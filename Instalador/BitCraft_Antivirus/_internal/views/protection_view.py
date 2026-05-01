import customtkinter as ctk

class ProtectionView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="Módulos de Protección",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)

        self.realtime_var = ctk.BooleanVar(value=False)
        self.realtime_switch = ctk.CTkSwitch(self, text="Protección en Tiempo Real",
                                             variable=self.realtime_var,
                                             command=self.toggle_realtime)
        self.realtime_switch.pack(pady=15)

        self.ransom_var = ctk.BooleanVar(value=False)
        self.ransom_switch = ctk.CTkSwitch(self, text="Anti-Ransomware",
                                          variable=self.ransom_var,
                                          command=self.toggle_ransomware)
        self.ransom_switch.pack(pady=15)

        self.behavior_var = ctk.BooleanVar(value=False)
        self.behavior_switch = ctk.CTkSwitch(self, text="Monitoreo de Comportamiento",
                                            variable=self.behavior_var,
                                            command=self.toggle_behavior)
        self.behavior_switch.pack(pady=15)

    def toggle_realtime(self):
        action = "start_realtime" if self.realtime_var.get() else "stop_realtime"
        self.bridge.send_command({"action": action}, wait_for_response=False)

    def toggle_ransomware(self):
        action = "ransom_on" if self.ransom_var.get() else "ransom_off"
        self.bridge.send_command({"action": action}, wait_for_response=False)

    def toggle_behavior(self):
        # En una versión avanzada esto iniciaría monitoreo de procesos
        print("Monitoreo de comportamiento:", self.behavior_var.get())