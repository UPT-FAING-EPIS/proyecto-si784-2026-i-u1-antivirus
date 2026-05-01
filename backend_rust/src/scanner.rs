use walkdir::WalkDir;
use std::fs;
use std::path::PathBuf;
use std::sync::Mutex;
use sha2::{Sha256, Digest};
use serde_json::{Value, json};
use crate::utils::{ok_response, error_response};

static OFFLINE_HASHES: Mutex<Vec<String>> = Mutex::new(Vec::new());

pub struct Threat {
    pub file: String,
    pub hash: String,
    pub threat_type: String,
    pub confidence: f32,
}

pub fn initialize_with_offline_signatures(sig_dir: &str) -> Result<(), Box<dyn std::error::Error>> {
    let hash_path = PathBuf::from(sig_dir).join("malware_hashes.txt");
    if hash_path.exists() {
        let content = fs::read_to_string(&hash_path)?;
        let mut hashes = OFFLINE_HASHES.lock().unwrap();
        hashes.clear();
        for line in content.lines() {
            let line = line.trim();
            if !line.is_empty() && !line.starts_with('#') {
                hashes.push(line.to_lowercase());
            }
        }
    }
    Ok(())
}

pub fn scan_directory(path: &str) -> Value {
    let target = PathBuf::from(path);
    if !target.exists() {
        return error_response("La ruta no existe");
    }

    let mut files = Vec::new();
    for entry in WalkDir::new(&target).follow_links(false).into_iter().filter_map(|e| e.ok()) {
        if entry.path().is_file() {
            files.push(entry.path().to_path_buf());
        }
    }

    match scan_files(&files) {
        Ok(threats) => {
            let result = json!({
                "action": "scan_complete",
                "scanned_files": files.len(),
                "threats_found": threats.len(),
                "threats": threats.iter().map(|t| {
                    json!({
                        "file": t.file,
                        "hash": t.hash,
                        "threat": t.threat_type,
                        "confidence": t.confidence
                    })
                }).collect::<Vec<_>>()
            });
            ok_response(result)
        }
        Err(e) => error_response(&format!("Error en escaneo: {}", e)),
    }
}

pub fn scan_files(paths: &[PathBuf]) -> Result<Vec<Threat>, Box<dyn std::error::Error>> {
    let mut threats = Vec::new();
    let hashes = OFFLINE_HASHES.lock().unwrap();
    
    for path in paths {
        let data = match fs::read(path) {
            Ok(d) => d,
            Err(_) => continue,
        };
        
        let mut hasher = Sha256::new();
        hasher.update(&data);
        let hash = hex::encode(hasher.finalize());
        
        // 1. Verificación de hash
        if hashes.contains(&hash) {
            threats.push(Threat {
                file: path.display().to_string(),
                hash: hash.clone(),
                threat_type: "Malware conocido (hash)".to_string(),
                confidence: 1.0,
            });
            continue;
        }
        
        // 2. Heurística de entropía
        if data.len() > 1024 {
            let entropy = calculate_entropy(&data);
            if entropy > 7.5 && is_pe_file(&data) {
                threats.push(Threat {
                    file: path.display().to_string(),
                    hash: hash.clone(),
                    threat_type: "Sospechoso (alta entropía + PE)".to_string(),
                    confidence: 0.5,
                });
                continue;
            }
        }
        
        // 3. Detección de strings sospechosos
        if let Ok(text) = String::from_utf8(data[..std::cmp::min(4096, data.len())].to_vec()) {
            let suspicious = ["CreateRemoteThread", "VirtualAllocEx", "WriteProcessMemory",
                              "powershell -enc", "Invoke-Mimikatz", "ransom", "bitcoin_wallet"];
            let mut found = Vec::new();
            for s in &suspicious {
                if text.to_lowercase().contains(&s.to_lowercase()) {
                    found.push(*s);
                }
            }
            if found.len() >= 3 {
                threats.push(Threat {
                    file: path.display().to_string(),
                    hash: hash.clone(),
                    threat_type: format!("Sospechoso (strings: {})", found.join(", ")),
                    confidence: 0.6,
                });
            }
        }
    }
    
    Ok(threats)
}

fn calculate_entropy(data: &[u8]) -> f64 {
    let mut freq = [0u32; 256];
    for &byte in data {
        freq[byte as usize] += 1;
    }
    let len = data.len() as f64;
    let mut entropy = 0.0;
    for &count in &freq {
        if count > 0 {
            let p = count as f64 / len;
            entropy -= p * p.log2();
        }
    }
    entropy
}

fn is_pe_file(data: &[u8]) -> bool {
    data.len() >= 2 && data[0] == 0x4D && data[1] == 0x5A
}