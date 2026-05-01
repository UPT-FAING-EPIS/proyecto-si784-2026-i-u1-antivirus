use std::fs;
use std::path::{Path, PathBuf};
use sha2::{Sha256, Digest};
use serde_json::Value;
use crate::utils::{ok_response, error_response};

const QUARANTINE_DIR: &str = "C:\\ProgramData\\SecureGuard\\Quarantine";

pub fn quarantine_file(file_path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    if !file_path.exists() {
        return Err("File not found".into());
    }
    
    fs::create_dir_all(QUARANTINE_DIR)?;
    
    let data = fs::read(file_path)?;
    let hash = hex::encode(Sha256::digest(&data));
    let new_name = format!("{}.quar", hash);
    let dest = PathBuf::from(QUARANTINE_DIR).join(&new_name);
    
    fs::rename(file_path, &dest)?;
    
    let meta_path = dest.with_extension("meta");
    fs::write(meta_path, file_path.display().to_string())?;
    
    Ok(())
}

pub fn restore_file(quar_file: &str) -> Value {
    let quar_path = PathBuf::from(QUARANTINE_DIR).join(quar_file);
    if !quar_path.exists() {
        return error_response("Archivo de cuarentena no encontrado");
    }
    
    let meta_path = quar_path.with_extension("meta");
    if let Ok(original) = fs::read_to_string(&meta_path) {
        let original = PathBuf::from(original.trim());
        if let Some(parent) = original.parent() {
            fs::create_dir_all(parent).ok();
        }
        match fs::rename(&quar_path, &original) {
            Ok(_) => {
                fs::remove_file(meta_path).ok();
                ok_response(serde_json::json!({"restored": original.display().to_string()}))
            }
            Err(e) => error_response(&format!("Error al restaurar: {}", e)),
        }
    } else {
        error_response("Metadatos no encontrados")
    }
}

pub fn delete_quarantined(quar_file: &str) -> Value {
    let quar_path = PathBuf::from(QUARANTINE_DIR).join(quar_file);
    if quar_path.exists() {
        let meta = quar_path.with_extension("meta");
        fs::remove_file(&quar_path).ok();
        fs::remove_file(meta).ok();
        ok_response(serde_json::json!({"deleted": quar_file}))
    } else {
        error_response("Archivo no encontrado")
    }
}

pub fn list_quarantine() -> Vec<Value> {
    let mut items = Vec::new();
    if let Ok(entries) = fs::read_dir(QUARANTINE_DIR) {
        for entry in entries.flatten() {
            let path = entry.path();
            if path.extension().map_or(false, |e| e == "quar") {
                let meta = path.with_extension("meta");
                let original = fs::read_to_string(&meta).unwrap_or_else(|_| "Desconocido".to_string());
                let metadata = fs::metadata(&path).ok();
                let size = metadata.map(|m| m.len()).unwrap_or(0);
                items.push(serde_json::json!({
                    "file": path.file_name().unwrap().to_string_lossy(),
                    "original": original.trim(),
                    "size_bytes": size
                }));
            }
        }
    }
    items
}