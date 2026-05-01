use std::process::Command;
use serde_json::Value;
use crate::utils::{ok_response, error_response};

pub fn set_firewall(enable: bool) -> Value {
    let action = if enable { "enable" } else { "disable" };
    let output = Command::new("netsh")
        .args(&["advfirewall", "set", "allprofiles", "state", if enable { "on" } else { "off" }])
        .output();

    match output {
        Ok(out) => {
            if out.status.success() {
                ok_response(serde_json::json!({"firewall": action, "message": format!("Firewall {}", action)}))
            } else {
                let stderr = String::from_utf8_lossy(&out.stderr);
                error_response(&format!("Error al cambiar firewall: {}", stderr))
            }
        }
        Err(e) => error_response(&format!("Error ejecutando netsh: {}", e)),
    }
}