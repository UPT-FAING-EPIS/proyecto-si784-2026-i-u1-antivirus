use std::sync::mpsc::channel;
use std::thread;
use std::path::PathBuf;
use notify::{Event, RecursiveMode, Watcher};
use serde_json::{Value, json};
use crate::scanner;
use crate::quarantine;
use crate::updater;
use crate::network;
use crate::cleaner;
use crate::utils::{ok_response, error_response};

static mut EVENT_SENDER: Option<std::sync::mpsc::Sender<String>> = None;

pub fn handle_command(cmd_json: &str) -> Value {
    let cmd: Value = serde_json::from_str(cmd_json).unwrap_or(json!({"action":"unknown"}));
    
    match cmd["action"].as_str().unwrap_or("") {
        "start_realtime" => start_file_monitor(),
        "stop_realtime" => {
            ok_response(json!({"message": "Real-time protection stopped"}))
        }
        "scan" => {
            let path = cmd["path"].as_str().unwrap_or("C:\\Users");
            scanner::scan_directory(path)
        }
        "clean" => cleaner::clean_temp_files(),
        "firewall_on" => network::set_firewall(true),
        "firewall_off" => network::set_firewall(false),
        "update" => updater::update_signatures(),
        "restore_quarantine" => {
            let file = cmd["file"].as_str().unwrap_or("");
            quarantine::restore_file(file)
        }
        "delete_quarantine" => {
            let file = cmd["file"].as_str().unwrap_or("");
            quarantine::delete_quarantined(file)
        }
        "list_quarantine" => {
            let items = quarantine::list_quarantine();
            ok_response(json!({"items": items}))
        }
        _ => error_response("Unknown daemon command"),
    }
}

fn start_file_monitor() -> Value {
    let (tx, _rx) = channel();
    unsafe { EVENT_SENDER = Some(tx); }

    thread::spawn(move || {
        let mut watcher = notify::recommended_watcher(move |res: Result<Event, notify::Error>| {
            match res {
                Ok(event) => {
                    if event.kind.is_create() || event.kind.is_modify() {
                        for path in event.paths {
                            if let Err(e) = process_new_file(&path) {
                                eprintln!("Error processing {:?}: {}", path, e);
                            }
                        }
                    }
                }
                Err(e) => eprintln!("watch error: {:?}", e),
            }
        }).unwrap();

        let dirs_to_watch = [
            dirs::document_dir().unwrap_or(PathBuf::from("C:\\Users")),
            dirs::download_dir().unwrap_or(PathBuf::from("C:\\Users\\Downloads")),
            PathBuf::from("C:\\Users\\Public"),
        ];
        
        for dir in &dirs_to_watch {
            watcher.watch(dir, RecursiveMode::NonRecursive).ok();
        }

        loop { std::thread::park(); }
    });

    ok_response(json!({"message": "Real-time protection started"}))
}

fn process_new_file(path: &PathBuf) -> Result<(), Box<dyn std::error::Error>> {
    let threats = scanner::scan_files(&[path.clone()])?;
    for threat in threats {
        quarantine::quarantine_file(&PathBuf::from(&threat.file))?;
        if let Some(ref tx) = unsafe { EVENT_SENDER.as_ref() } {
            let alert = json!({
                "event": "threat_detected",
                "file": threat.file,
                "hash": threat.hash,
                "threat": threat.threat_type,
                "confidence": threat.confidence
            });
            tx.send(alert.to_string()).ok();
        }
    }
    Ok(())
}

pub fn send_event(event: Value) {
    if let Some(ref tx) = unsafe { EVENT_SENDER.as_ref() } {
        tx.send(event.to_string()).ok();
    }
}