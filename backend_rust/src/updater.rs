use std::fs;
use std::path::PathBuf;
use serde_json::Value;
use crate::utils::{ok_response, error_response};

const UPDATE_URL_HASHES: &str = "https://raw.githubusercontent.com/TU_USUARIO/SecureGuard-Signatures/main/malware_hashes.txt";
const UPDATE_URL_YARA: &str = "https://raw.githubusercontent.com/TU_USUARIO/SecureGuard-Signatures/main/yara_rules.yar";
const LOCAL_SIG_DIR: &str = "signatures/";

pub fn update_signatures() -> Value {
    fs::create_dir_all(LOCAL_SIG_DIR).ok();
    
    let mut updated = false;
    let mut messages = Vec::new();
    
    match reqwest::blocking::get(UPDATE_URL_HASHES) {
        Ok(response) => {
            if response.status().is_success() {
                if let Ok(text) = response.text() {
                    let path = PathBuf::from(LOCAL_SIG_DIR).join("malware_hashes.txt");
                    if fs::write(&path, &text).is_ok() {
                        updated = true;
                        messages.push(format!("Hashes actualizados: {} lineas", text.lines().count()));
                    }
                }
            }
        }
        Err(e) => {
            messages.push(format!("Error descargando hashes: {}", e));
        }
    }
    
    match reqwest::blocking::get(UPDATE_URL_YARA) {
        Ok(response) => {
            if response.status().is_success() {
                if let Ok(text) = response.text() {
                    let path = PathBuf::from(LOCAL_SIG_DIR).join("yara_rules.yar");
                    if fs::write(&path, &text).is_ok() {
                        updated = true;
                        messages.push("Reglas YARA actualizadas".to_string());
                    }
                }
            }
        }
        Err(e) => {
            messages.push(format!("Error descargando YARA: {}", e));
        }
    }
    
    if updated {
        ok_response(serde_json::json!({
            "updated": true,
            "message": format!("Firmas actualizadas: {}", messages.join(" | "))
        }))
    } else if messages.is_empty() {
        ok_response(serde_json::json!({
            "updated": false,
            "message": "No se encontraron actualizaciones nuevas"
        }))
    } else {
        error_response(&format!("Errores: {}", messages.join(" | ")))
    }
}