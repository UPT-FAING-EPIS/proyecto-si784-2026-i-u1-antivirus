import customtkinter as ctk
import threading

class QuarantineView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="Archivos en Cuarentena",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

        self.listbox = ctk.CTkTextbox(self, width=600, height=300)
        self.listbox.pack(pady=10)

        self.refresh_btn = ctk.CTkButton(self, text="Actualizar lista", command=self.load_quarantine)
        self.refresh_btn.pack(pady=5)

        self.restore_btn = ctk.CTkButton(self, text="Restaurar seleccionado", command=self.restore_selected)
        self.restore_btn.pack(pady=5)

        self.delete_btn = ctk.CTkButton(self, text="Eliminar seleccionado", command=self.delete_selected)
        self.delete_btn.pack(pady=5)

        self.load_quarantine()

    def load_quarantine(self):
        # Pedimos al motor la lista (simplemente leemos archivos .quar, pero podemos implementar un comando)
        # Como no hemos implementado un comando "list_quarantine" en Rust, usamos una llamada genérica vacía.
        # Para este ejemplo, el motor no tiene list, así que mostramos un placeholder.
        # En una versión real, enviaríamos {"action": "list_quarantine"} y lo implementaríamos en daemon.
        self.listbox.delete("1.0", "end")
        self.listbox.insert("end", "Función no implementada en backend aún.\n")

    def restore_selected(self):
        # Implementar usando bridge
        pass

    def delete_selected(self):
        pass