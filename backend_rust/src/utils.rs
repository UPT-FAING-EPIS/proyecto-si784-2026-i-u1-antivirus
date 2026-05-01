use serde_json::Value;

pub fn ok_response(data: Value) -> Value {
    let base = serde_json::json!({"status": "success"});
    if let Value::Object(mut map) = base {
        if let Value::Object(data_map) = data {
            for (k, v) in data_map {
                map.insert(k, v);
            }
        }
        Value::Object(map)
    } else {
        base
    }
}

pub fn error_response(msg: &str) -> Value {
    serde_json::json!({"status": "error", "message": msg})
}