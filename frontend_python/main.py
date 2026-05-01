# frontend_python/main.py
import customtkinter as ctk
from views.dashboard_view import DashboardView
from views.protection_view import ProtectionView
from views.settings_view import SettingsView
from views.quarantine_view import QuarantineView
from views.cleaning_view import CleaningView
from views.update_view import UpdateView
from engine_bridge import EngineBridge
from utils import resource_path
import sys
import os

# Configurar apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SecureGuardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SecureGuard Security")
        self.geometry("950x650")
        self.minsize(850, 600)

        # Inicializar el puente con el motor (backend)
        self.bridge = EngineBridge()
        try:
            self.bridge.start_daemon()
            print("[SecureGuard] Motor iniciado correctamente")
        except RuntimeError as e:
            print(f"[SecureGuard] Error iniciando motor: {e}")

        # Configurar grid principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(7, weight=1)

        # Logo
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="🛡️ SecureGuard",
            font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones de navegación
        buttons = [
            ("🏠  Inicio", self.show_dashboard),
            ("🛡️  Protección", self.show_protection),
            ("🌐  Firewall", self.show_firewall),
            ("🧹  Limpieza", self.show_cleaning),
            ("🔒  Cuarentena", self.show_quarantine),
            ("🔄  Actualizar", self.show_update),
            ("⚙️  Configuración", self.show_settings),
        ]

        for i, (text, command) in enumerate(buttons):
            btn = ctk.CTkButton(
                self.sidebar, text=text, command=command,
                fg_color="transparent", border_width=1,
                text_color=("gray10", "#DCE4EE"),
                anchor="w", height=35)
            btn.grid(row=i+1, column=0, padx=15, pady=5, sticky="ew")

        # Frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Vistas
        self.views = {}
        self.show_dashboard()

    def clear_main_frame(self):
        """Limpia el frame principal antes de cambiar de vista"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main_frame()
        view = DashboardView(self.main_frame, self.bridge)
        view.pack(fill="both", expand=True)
        self.views['dashboard'] = view

    def show_protection(self):
        self.clear_main_frame()
        view = ProtectionView(self.main_frame, self.bridge)
        view.pack(fill="both", expand=True)
        self.views['protection'] = view

    def show_firewall(self):
        self.clear_main_frame()
        from views.settings_view import SettingsView
        view = SettingsView(self.main_frame, self.bridge, only_firewall=True)
        view.pack(fill="both", expand=True)
        self.views['firewall'] = view

    def show_cleaning(self):
        self.clear_main_frame()
        view = CleaningView(self.main_frame, self.bridge)
        view.pack(fill="both", expand=True)
        self.views['cleaning'] = view

    def show_quarantine(self):
        self.clear_main_frame()
        view = QuarantineView(self.main_frame, self.bridge)
        view.pack(fill="both", expand=True)
        self.views['quarantine'] = view

    def show_update(self):
        self.clear_main_frame()
        view = UpdateView(self.main_frame, self.bridge)
        view.pack(fill="both", expand=True)
        self.views['update'] = view

    def show_settings(self):
        self.clear_main_frame()
        view = SettingsView(self.main_frame, self.bridge, only_firewall=False)
        view.pack(fill="both", expand=True)
        self.views['settings'] = view

    def on_closing(self):
        """Se ejecuta al cerrar la ventana"""
        print("[SecureGuard] Cerrando aplicación...")
        self.bridge.stop_daemon()
        self.destroy()


if __name__ == "__main__":
    app = SecureGuardApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()