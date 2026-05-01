import customtkinter as ctk
import psutil
import threading

class SettingsView(ctk.CTkFrame):
    def __init__(self, parent, bridge, only_firewall=False):
        super().__init__(parent)
        self.bridge = bridge

        if only_firewall:
            ctk.CTkLabel(self, text="Firewall de Windows",
                         font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)
            self.firewall_var = ctk.BooleanVar(value=True)
            self.firewall_switch = ctk.CTkSwitch(self, text="Activar Firewall",
                                                variable=self.firewall_var,
                                                command=self.toggle_firewall)
            self.firewall_switch.pack(pady=20)
        else:
            ctk.CTkLabel(self, text="Información del Sistema",
                         font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
            # Hardware info como antes, más firewall
            hw_frame = ctk.CTkFrame(self)
            hw_frame.pack(pady=10, padx=20, fill="x")
            cpu = psutil.cpu_percent(interval=0.1)
            ctk.CTkLabel(hw_frame, text=f"CPU: {cpu}%").pack(anchor="w", padx=15, pady=5)
            mem = psutil.virtual_memory()
            ctk.CTkLabel(hw_frame, text=f"RAM: {mem.used//(1024**2)} MB / {mem.total//(1024**2)} MB ({mem.percent}%)").pack(anchor="w", padx=15, pady=5)
            
            # Disco con manejo de error
            try:
                disk = psutil.disk_usage('C:\\')
                disk_text = f"Disco C: {disk.free//(1024**3)} GB libre de {disk.total//(1024**3)} GB"
            except:
                disk_text = "Disco: Información no disponible"
            
            ctk.CTkLabel(hw_frame, text=disk_text).pack(anchor="w", padx=15, pady=5)

            ctk.CTkLabel(self, text="").pack(pady=10)
            ctk.CTkLabel(self, text="Firewall", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
            self.firewall_var = ctk.BooleanVar(value=True)
            self.firewall_switch = ctk.CTkSwitch(self, text="Firewall de Windows",
                                                variable=self.firewall_var,
                                                command=self.toggle_firewall)
            self.firewall_switch.pack(pady=10)

    def toggle_firewall(self):
        action = "firewall_on" if self.firewall_var.get() else "firewall_off"
        self.bridge.send_command({"action": action}, wait_for_response=False)