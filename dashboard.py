import os
import sys
import subprocess
import tkinter.messagebox as messagebox
import customtkinter as ctk
from lerning_module import LearningModule

ROLES_INFO = {
    "Alcalde": {
        "descripcion": "Representante elegido que dirige la visión y las políticas de la ciudad.",
    },
    "Ingeniero Urbano": {
        "descripcion": "Experto técnico en diseño, construcción y mantenimiento.",
    },
    "Director Económico": {
        "descripcion": "Encargado de la salud financiera y el desarrollo económico.",
    }
}

class DashboardWindow(ctk.CTk):
    def __init__(self, user_email: str, role: str):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.user_email = user_email
        self.title(f"Neocity — Panel ({role})")
        self.geometry("1200x768")
        self.resizable(True, True)

        # Fuentes
        self.font_title = ctk.CTkFont(family="Consolas", size=36, weight="bold")
        self.font_header = ctk.CTkFont(family="Consolas", size=20, weight="bold")
        self.font_normal = ctk.CTkFont(family="Consolas", size=15)
        self.font_desc = ctk.CTkFont(family="Consolas", size=15)

        # Estado selección
        self.selected_role = None
        self._card_frames = {}

        self.setup_ui(user_email, role)

    def setup_ui(self, user_email, role):

        # Container principal
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=15, pady=15)

        # Header
        header = ctk.CTkLabel(main,
                            text=f"Bienvenido {user_email}",
                            font=self.font_title,
                            text_color="#00ffd8")
        header.pack(pady=10)

        # Frame para roles
        roles_frame = ctk.CTkFrame(main, fg_color="#081421", corner_radius=15)
        roles_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título de selección
        select_title = ctk.CTkLabel(roles_frame,
                                  text="SELECCIONA TU ROL EN NEOCITY",
                                  font=self.font_header,
                                  text_color="#bdfef0")
        select_title.pack(pady=15)

        # Frame para las tarjetas de rol
        cards_frame = ctk.CTkFrame(roles_frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=10)
        cards_frame.grid_columnconfigure((0,1,2), weight=1)

        # Info panel para mostrar detalles del rol
        self.info_panel = ctk.CTkTextbox(roles_frame,
                                        height=90,
                                        font=self.font_desc,
                                        fg_color="#061018",
                                        text_color="#8ef5e6",
                                        corner_radius=8)
        self.info_panel.pack(fill="x", padx=20, pady=10)

        # Crear tarjetas para cada rol
        for i, (rol, info) in enumerate(ROLES_INFO.items()):
            self.create_role_card(cards_frame, rol, info, i)

        # Botones de acción
        btn_frame = ctk.CTkFrame(roles_frame, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=0)

        select_btn = ctk.CTkButton(btn_frame,
                                 text="Comenzar con el rol seleccionado",
                                 command=self.select_role,
                                 font=self.font_normal,
                                 fg_color="#00bfa5",
                                 hover_color="#00e0c6")
        select_btn.pack(side="left", padx=10)

        logout_btn = ctk.CTkButton(btn_frame,
                                 text="Cerrar Sesión",
                                 command=self.on_logout,
                                 font=self.font_normal,
                                 fg_color="#ff6961",
                                 hover_color="#ff8a84")
        logout_btn.pack(side="right", padx=10)

        learning_btn = ctk.CTkButton(
            main,
            text="📘 Módulo de Aprendizaje",
            command=lambda: LearningModule(self),
            font=self.font_normal,
            fg_color="#005f73",
            hover_color="#0a9396"
        )
        learning_btn.pack(pady=5, anchor="ne")


    def create_role_card(self, parent, rol, info, col):
        card = ctk.CTkFrame(parent, fg_color="#0a1824", corner_radius=10)
        card.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")
        self._card_frames[rol] = card

        title = ctk.CTkLabel(card,
                           text=rol,
                           font=self.font_header,
                           text_color="#00ffd8")
        title.pack(pady=10)

        desc = ctk.CTkLabel(card,
                          text=info["descripcion"],
                          font=self.font_desc,
                          text_color="#bdfef0")
        desc.pack(pady=5)

        def show_info():
            self.info_panel.delete("1.0", "end")
            self.info_panel.insert("1.0",
f"""ROL: {rol}
{info['descripcion']}
""")
            # marcar como seleccionado visualmente cuando se ve detalle
            self._set_selected(rol)

        info_btn = ctk.CTkButton(card,
                               text="Ver / Seleccionar",
                               command=show_info,
                               font=self.font_normal,
                               fg_color="#013338",
                               hover_color="#014a44")
        info_btn.pack(pady=10)

    def _set_selected(self, rol):
        # Resaltar tarjeta seleccionada y almacenar elección
        self.selected_role = rol
        for r, frame in self._card_frames.items():
            if r == rol:
                frame.configure(fg_color="#083237")  # resaltado
            else:
                frame.configure(fg_color="#0a1824")  # normal

    def select_role(self):
        if not self.selected_role:
            messagebox.showwarning("Selecciona un rol", "Primero selecciona un rol haciendo clic en 'Ver / Seleccionar'.")
            return
        # Confirmación
        ok = messagebox.askyesno("Confirmar rol", f"Has elegido '{self.selected_role}'. ¿Deseas comenzar el juego con este rol?")
        if not ok:
            return

        # Ejecutar el juego en un proceso separado con los argumentos: email y rol
        try:
            # usar el mismo intérprete de Python
            cwd = os.path.dirname(os.path.abspath(__file__))
            subprocess.Popen([sys.executable, os.path.join(cwd, "game.py"), self.user_email, self.selected_role], cwd=cwd)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar el juego: {e}")
            return

        # Mensaje de bienvenida breve y opcionalmente cerrar dashboard
        messagebox.showinfo("Bienvenido a Neocity", f"Bienvenido a Neocity, {self.user_email}.\nHas iniciado como: {self.selected_role}\nSe abrirá la ventana del juego.")
        # opcional: cerrar dashboard cuando el juego se lanza
        # self.destroy()

        

    def on_logout(self):
        self.destroy()

if __name__ == "__main__":
    app = DashboardWindow("test@email.com", "Usuario")
    app.mainloop()