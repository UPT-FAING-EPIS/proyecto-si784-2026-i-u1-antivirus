use serde_json::Value;
use crate::utils::ok_response;

pub fn enable_ransomware_protection() -> Value {
    ok_response(serde_json::json!({"ransomware": "enabled", "message": "Anti-ransomware activado"}))
}

pub fn disable_ransomware_protection() -> Value {
    ok_response(serde_json::json!({"ransomware": "disabled", "message": "Anti-ransomware desactivado"}))
}