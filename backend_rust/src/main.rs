use std::io::{self, BufRead, Write};

mod scanner;
mod protection;
mod network;
mod utils;
mod daemon;
mod quarantine;
mod cleaner;
mod updater;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    
    if args.len() < 2 {
        eprintln!("SecureGuard Engine v0.3.0");
        eprintln!("Uso: secureguard_engine [daemon|scan|clean|firewall_on|firewall_off|update|load_signatures]");
        return;
    }

    let command = &args[1];

    match command.as_str() {
        "daemon" => {
            println!("[SecureGuard] Iniciando motor en modo persistente...");
            let stdin = io::stdin();
            let mut stdout = io::stdout();
            
            let sig_path = args.get(2).cloned().unwrap_or_else(|| "signatures/".to_string());
            if let Err(e) = scanner::initialize_with_offline_signatures(&sig_path) {
                eprintln!("[SecureGuard] Advertencia: No se pudieron cargar firmas offline: {}", e);
            } else {
                eprintln!("[SecureGuard] Firmas offline cargadas correctamente");
            }
            
            for line in stdin.lock().lines() {
                let line = line.unwrap();
                let response = daemon::handle_command(&line);
                writeln!(stdout, "{}", serde_json::to_string(&response).unwrap()).unwrap();
                stdout.flush().unwrap();
            }
        }
        "scan" => {
            let target = if args.len() > 2 { &args[2] } else { "C:\\Users" };
            let sig_path = args.get(3).unwrap_or(&"signatures/".to_string()).clone();
            scanner::initialize_with_offline_signatures(&sig_path).ok();
            let result = scanner::scan_directory(target);
            println!("{}", serde_json::to_string(&result).unwrap());
        }
        "update" => {
            let result = updater::update_signatures();
            println!("{}", serde_json::to_string(&result).unwrap());
        }
        "clean" => {
            let result = cleaner::clean_temp_files();
            println!("{}", serde_json::to_string(&result).unwrap());
        }
        "firewall_on" => println!("{}", network::set_firewall(true)),
        "firewall_off" => println!("{}", network::set_firewall(false)),
        _ => {
            let err = serde_json::json!({"status": "error", "message": "Comando no reconocido"});
            println!("{}", err);
        }
    }
}