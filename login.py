import os
import json
import sys
import tkinter as tk
import tkinter.messagebox as messagebox
import customtkinter as ctk

USERS_FILE = "neocity_users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Apariencia
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Ventana más amplia
        self.WIDTH = 1100
        self.HEIGHT = 700
        self.title("Neocity – Iniciar sesión / Registro")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.center_window()

        # Fuentes (estilo "gordas y cuadradas" usando Consolas/monospace)
        self.font_title = ctk.CTkFont(family="Consolas", size=56, weight="bold")
        self.font_logo = ctk.CTkFont(family="Consolas", size=28, weight="bold")
        self.font_label = ctk.CTkFont(family="Consolas", size=14, weight="bold")
        self.font_input = ctk.CTkFont(family="Consolas", size=16)

        # Cargar usuarios
        self.users = load_users()

        self.setup_ui()

        self._after_ids = []          # <-- almacenar ids de after
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.WIDTH // 2)
        y = (self.winfo_screenheight() // 2) - (self.HEIGHT // 2)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

    def setup_ui(self):
        # Contenedor principal con dos columnas: panel decorativo + formulario
        main = ctk.CTkFrame(self, corner_radius=0, fg_color="#0b1020")
        main.pack(fill="both", expand=True)

        main.grid_rowconfigure(0, weight=1)
        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=2)

        # PANEL IZQUIERDO - estética futurista
        left = ctk.CTkFrame(main, corner_radius=12, fg_color="#07101a")
        left.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

        left.grid_rowconfigure(0, weight=0)
        left.grid_rowconfigure(1, weight=1)
        left.grid_rowconfigure(2, weight=0)

        # Logo grande estilo bloque
        logo = ctk.CTkLabel(left, text="NEOCITY", font=self.font_title, text_color="#00ffd8")
        logo.grid(row=0, column=0, pady=(30,10), padx=20)

        # Imagen / arte ascii / descripción
        neon_box = ctk.CTkTextbox(left, width=360, height=340, corner_radius=8, fg_color="#021018", text_color="#8ef5e6", border_color="#00ffd8", border_width=1)
        neon_box.grid(row=1, column=0, padx=20, pady=10)
        neon_box.insert("0.0",
"""
    BIENVENIDO A NEOCITY               
    Futurista · Pixel · Minimal     
    Accede como Usuario o Administrador""")
        neon_box.configure(state="disabled", font=self.font_label)

        footer = ctk.CTkLabel(left, text="© Neocity 2025", font=self.font_logo, text_color="#66ffe0")
        footer.grid(row=2, column=0, pady=(10,30))

        # PANEL DERECHO - formulario amplio
        right = ctk.CTkFrame(main, corner_radius=12, fg_color="#06121a")
        right.grid(row=0, column=1, sticky="nsew", padx=(0,30), pady=30)

        right.grid_columnconfigure(0, weight=1)
        form = ctk.CTkFrame(right, corner_radius=10, fg_color="#081421")
        form.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        # Encabezado formulario
        hdr = ctk.CTkLabel(form, text="ACCEDE A TU CUENTA", font=self.font_logo, text_color="#bdfef0")
        hdr.grid(row=0, column=0, columnspan=2, pady=(10,20))

        # Email
        lbl_email = ctk.CTkLabel(form, text="Correo electrónico", font=self.font_label, text_color="#b0fff0")
        lbl_email.grid(row=1, column=0, sticky="w", padx=10, pady=(6,2))
        self.email_input = ctk.CTkEntry(form, placeholder_text="ejemplo@dominio.com", width=480, height=40, font=self.font_input, border_width=1, corner_radius=8)
        self.email_input.grid(row=2, column=0, padx=10, pady=(0,10))

        # Contraseña con toggle
        lbl_pass = ctk.CTkLabel(form, text="Contraseña", font=self.font_label, text_color="#b0fff0")
        lbl_pass.grid(row=3, column=0, sticky="w", padx=10, pady=(6,2))
        pass_frame = ctk.CTkFrame(form, fg_color="transparent")
        pass_frame.grid(row=4, column=0, padx=10, pady=(0,10), sticky="w")
        self.pass_input = ctk.CTkEntry(pass_frame, placeholder_text="Contraseña", show="*", width=420, height=40, font=self.font_input, corner_radius=8)
        self.pass_input.pack(side="left")
        self.show_btn = ctk.CTkButton(pass_frame, text="Mostrar", width=60, height=38, command=self.toggle_password, fg_color="#013338", hover_color="#014a44", text_color="#9ff7ee", corner_radius=8)
        self.show_btn.pack(side="left", padx=(8,0))

        # Rol
        lbl_role = ctk.CTkLabel(form, text="Rol", font=self.font_label, text_color="#b0fff0")
        lbl_role.grid(row=5, column=0, sticky="w", padx=10, pady=(6,2))
        self.role_menu = ctk.CTkOptionMenu(form, values=["Usuario", "Administrador"], width=240, fg_color="#012428", button_color="#013338", dropdown_hover_color="#014a44", text_color="#dffcf7")
        self.role_menu.set("Usuario")
        self.role_menu.grid(row=6, column=0, padx=10, pady=(0,10), sticky="w")

        # Mensaje de ayuda / estado
        self.status_lbl = ctk.CTkLabel(form, text="", font=self.font_label, text_color="#8ef5e6")
        self.status_lbl.grid(row=7, column=0, padx=10, pady=(6,6), sticky="w")

        # Botones principales - estilo futurista y amplio
        btns = ctk.CTkFrame(form, fg_color="transparent")
        btns.grid(row=8, column=0, pady=(10,10), padx=10, sticky="ew")
        btns.grid_columnconfigure(0, weight=1)
        btns.grid_columnconfigure(1, weight=1)

        self.login_btn = ctk.CTkButton(btns, text="INICIAR SESIÓN", command=self.check_login, fg_color="#00ffe5", hover_color="#66fff0", text_color="#001", corner_radius=10, height=48, font=self.font_label)
        self.login_btn.grid(row=0, column=0, padx=(0,8), sticky="ew")
        self.register_btn = ctk.CTkButton(btns, text="REGISTRARSE", command=self.register_account, fg_color="#00bfa5", hover_color="#00e0c6", text_color="#001", corner_radius=10, height=48, font=self.font_label)
        self.register_btn.grid(row=0, column=1, padx=(8,0), sticky="ew")

        # Pequeño footer con atajos
        shortcuts = ctk.CTkLabel(right, text="Tips: usa correo válido • Contraseña mínima 4 caracteres", font=self.font_label, text_color="#64f1dd")
        shortcuts.grid(row=1, column=0, pady=(0,20), padx=40, sticky="s")

        # Bind Enter key para login rápido
        self.bind("<Return>", lambda e: self.check_login())

    def toggle_password(self):
        if self.pass_input.cget("show") == "":
            self.pass_input.configure(show="*")
            self.show_btn.configure(text="Mostrar")
        else:
            self.pass_input.configure(show="")
            self.show_btn.configure(text="Ocultar")

    def check_login(self):
        email = self.email_input.get().strip()
        password = self.pass_input.get()
        role = self.role_menu.get()

        if not email:
            messagebox.showwarning("Error", "Ingresa un correo electrónico")
            self.status_lbl.configure(text="Ingresa un correo.")
            return
        if email not in self.users:
            messagebox.showerror("Error", "Correo no registrado")
            self.status_lbl.configure(text="Correo no registrado.")
            return
        entry = self.users[email]
        if entry.get("password") != password or entry.get("role") != role:
            messagebox.showerror("Error", "Credenciales incorrectas o rol no coincide")
            self.status_lbl.configure(text="Credenciales incorrectas.")
            return

        # Credenciales válidas -> abrir dashboard (redirección)
        messagebox.showinfo("Bienvenido", f"Bienvenido {role} a Neocity, {email}")
        self.status_lbl.configure(text=f"Sesión iniciada como {role}.")
        self.open_dashboard(email, role)

    def open_dashboard(self, email, role):
        """
        Oculta la ventana de login e importa/ejecuta el módulo dashboard.py.
        Al cerrar el dashboard la ventana de login reaparece.
        """
        self.withdraw()  # ocultar ventana de login
        try:
            from dashboard import DashboardWindow
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el panel: {e}")
            self.deiconify()
            return

        # Crear y mostrar el dashboard (su propio mainloop)
        try:
            dash = DashboardWindow(user_email=email, role=role)
            dash.mainloop()
        finally:
            # Al cerrar el dashboard, mostrar login de nuevo
            try:
                self.deiconify()
            except:
                pass

    def register_account(self):
        email = self.email_input.get().strip()
        password = self.pass_input.get()
        role = self.role_menu.get()

        if not email or not password:
            messagebox.showwarning("Error", "Correo y contraseña son requeridos para registrarse")
            self.status_lbl.configure(text="Correo y contraseña son obligatorios.")
            return
        if len(password) < 4:
            messagebox.showwarning("Error", "La contraseña debe tener al menos 4 caracteres")
            self.status_lbl.configure(text="Contraseña demasiado corta.")
            return
        if email in self.users:
            messagebox.showerror("Error", "El correo ya está registrado")
            self.status_lbl.configure(text="Correo ya registrado.")
            return
        self.users[email] = {"password": password, "role": role}
        save_users(self.users)
        messagebox.showinfo("Registro exitoso", f"Se ha registrado el {role} {email}")
        self.status_lbl.configure(text=f"{role} registrado correctamente.")

    def schedule_after(self, ms, func, *args, **kwargs):
        """Programar un callback protegido; devuelve after_id."""
        def _wrapped():
            # si la ventana ya fue destruida, salir
            if not getattr(self, "winfo_exists", lambda: False)():
                return
            try:
                func(*args, **kwargs)
            except tk.TclError:
                # ignorar errores de Tcl (widget ya borrado)
                return
            except Exception:
                return
        after_id = self.after(ms, _wrapped)
        self._after_ids.append(after_id)
        return after_id

    def cancel_scheduled(self, after_id):
        try:
            self.after_cancel(after_id)
        except Exception:
            pass
        try:
            self._after_ids.remove(after_id)
        except ValueError:
            pass

    def on_close(self):
        # cancelar todos los callbacks pendientes antes de destruir
        for aid in list(self._after_ids):
            try:
                self.after_cancel(aid)
            except Exception:
                pass
        self._after_ids.clear()
        try:
            self.destroy()
        except Exception:
            pass

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()