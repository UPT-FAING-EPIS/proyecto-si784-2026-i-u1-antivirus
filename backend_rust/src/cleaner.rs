use std::fs;
use std::path::PathBuf;
use serde_json::Value;
use crate::utils::ok_response;

pub fn clean_temp_files() -> Value {
    let tmp_dirs = vec![
        PathBuf::from("C:\\Windows\\Temp"),
        PathBuf::from(std::env::var("TEMP").unwrap_or_else(|_| "C:\\Temp".to_string())),
    ];
    let mut deleted_count = 0;
    for dir in tmp_dirs {
        if let Ok(entries) = fs::read_dir(&dir) {
            for entry in entries.flatten() {
                let path = entry.path();
                if path.is_file() {
                    if fs::remove_file(&path).is_ok() {
                        deleted_count += 1;
                    }
                } else if path.is_dir() {
                    let _ = fs::remove_dir_all(&path);
                    deleted_count += 1;
                }
            }
        }
    }
    ok_response(serde_json::json!({
        "cleaned": deleted_count,
        "message": format!("{} archivos/carpetas temporales eliminados", deleted_count)
    }))
}