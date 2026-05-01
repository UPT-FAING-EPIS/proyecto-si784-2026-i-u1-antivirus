import customtkinter as ctk
import threading

class UpdateView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="Actualización de Firmas",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)

        self.status_label = ctk.CTkLabel(self, text="Firmas: Listas para actualizar",
                                         font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=15)

        self.update_btn = ctk.CTkButton(
            self, text="Buscar e Instalar Actualizaciones",
            command=self.start_update, width=250, height=40)
        self.update_btn.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)
        self.progress.pack(pady=10)
        self.progress.pack_forget()

        self.detail_text = ctk.CTkTextbox(self, width=500, height=200)
        self.detail_text.pack(pady=20)
        self.detail_text.insert("end", "Historial de actualizaciones:\n")
        self.detail_text.insert("end", "- Firmas base incluidas (offline)\n")
        self.detail_text.insert("end", "- Conecte a internet para actualizar\n")

    def start_update(self):
        self.update_btn.configure(state="disabled", text="Actualizando...")
        self.progress.pack()
        self.progress.start()
        threading.Thread(target=self.run_update, daemon=True).start()

    def run_update(self):
        result = self.bridge.send_command({"action": "update"}, timeout=60)
        self.after(0, self.update_finished, result)

    def update_finished(self, result):
        self.progress.stop()
        self.progress.pack_forget()
        self.update_btn.configure(state="normal", text="Buscar e Instalar Actualizaciones")
        
        if result.get("status") == "success":
            self.status_label.configure(text="✅ Firmas actualizadas correctamente")
            self.detail_text.insert("end", f"- {result.get('message', 'Actualización exitosa')}\n")
        else:
            self.status_label.configure(text="❌ Error en la actualización")
            self.detail_text.insert("end", f"- Error: {result.get('message', 'Desconocido')}\n")