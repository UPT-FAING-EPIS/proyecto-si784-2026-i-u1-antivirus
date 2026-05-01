import customtkinter as ctk
import threading

class CleaningView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="Limpieza del Sistema",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

        self.clean_btn = ctk.CTkButton(self, text="Limpiar archivos temporales",
                                       command=self.start_clean)
        self.clean_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def start_clean(self):
        self.clean_btn.configure(state="disabled", text="Limpiando...")
        threading.Thread(target=self.run_clean, daemon=True).start()

    def run_clean(self):
        result = self.bridge.send_command({"action": "clean"})
        self.after(0, self.clean_finished, result)

    def clean_finished(self, result):
        self.clean_btn.configure(state="normal", text="Limpiar archivos temporales")
        msg = result.get("message", "Operación completada")
        self.status_label.configure(text=msg)