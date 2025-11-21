import customtkinter as ctk

class LearningModule(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Módulo de Aprendizaje — Scrum y PMBOK")
        self.geometry("1000x700")
        self.resizable(True, True)
        ctk.set_appearance_mode("dark")

        # ======= ESTILOS =======
        self.font_title = ctk.CTkFont("Consolas", 30, "bold")
        self.font_subtitle = ctk.CTkFont("Consolas", 22, "bold")
        self.font_text = ctk.CTkFont("Consolas", 15)

        # ======= TÍTULO =======
        title = ctk.CTkLabel(
            self, 
            text="📘 Módulo de Aprendizaje",
            font=self.font_title,
            text_color="#00ffd8"
        )
        title.pack(pady=15)

        # ======= CONTENEDOR PRINCIPAL =======
        container = ctk.CTkFrame(self, fg_color="#061018")
        container.pack(fill="both", expand=True, padx=15, pady=15)

        # ======= MENÚ LATERAL =======
        sidebar = ctk.CTkFrame(container, width=200, fg_color="#0a1824")
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        # ======= CONTENIDO =======
        self.content = ctk.CTkTextbox(
            container,
            wrap="word",
            font=self.font_text,
            fg_color="#081421",
            text_color="#bdfef0"
        )
        self.content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # ======= BOTONES DEL MENÚ =======
        buttons = [
            ("📘 Introducción a Scrum", self.show_scrum_intro),
            ("🧩 Roles Scrum", self.show_scrum_roles),
            ("📆 Eventos Scrum", self.show_scrum_events),
            ("📦 Artefactos Scrum", self.show_scrum_artifacts),
            ("📙 PMBOK General", self.show_pmbok_intro),
            ("🗂 Áreas de Conocimiento", self.show_pmbok_areas),
            ("🏙 Relación con Roles", self.show_roles_relation)
        ]

        for text, cmd in buttons:
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=cmd,
                fg_color="#013338",
                hover_color="#02645a",
                font=self.font_text
            )
            btn.pack(fill="x", pady=6, padx=10)

    # ==================================================
    # ================== SECCIONES ======================
    # ==================================================

    def show_scrum_intro(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        📘════════════════════════════════════
                INTRODUCCIÓN A SCRUM
        ════════════════════════════════════📘

        Scrum es un marco ágil que organiza el trabajo en ciclos iterativos llamados 
        **Sprints**, permitiendo adaptarse rápidamente a los cambios y entregar valor 
        continuamente.

        Es ideal para:
        ✔ Proyectos con incertidumbre  
        ✔ Cambios constantes del cliente  
        ✔ Equipos dinámicos  

         — Representación de un equipo Scrum
                        _________
           (•‿•)     (•‿•)     (•‿•)
            /|\\       /|\\       /|\\
            / \\       / \\       / \\
        —— Trabajo colaborativo y ágil ——

        PRINCIPIOS FUNDAMENTALES:
        🔹 **Transparencia** — Todos conocen el estado del proyecto.  
        🔹 **Inspección** — Se revisa lo hecho en cada evento.  
        🔹 **Adaptación** — Se corrige el rumbo rápidamente.  

        VALORES DE SCRUM:
        💙 Compromiso  
        💚 Coraje  
        💛 Enfoque  
        💛 Respeto  
        💜 Apertura  

        Scrum impulsa equipos motivados, auto-organizados y enfocados en mejorar siempre.
        """
        )


    def show_scrum_roles(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        🧩══════════════════════════════
                ROLES EN SCRUM
        ══════════════════════════════🧩

        Scrum se compone de 3 roles esenciales que forman el **Scrum Team**.

        1️⃣ **PRODUCT OWNER (PO)**
        Responsable del valor del producto.
        
        Roles Scrum

               (⌐■_■)
                /|\\
                / \\      ← Product Owner

                (•ᴗ•)
               /(   )\\
                 / \\      ← Scrum Master

           (•‿•)   (•‿•)   (•‿•)
            /|\\     /|\\     /|\\
            / \\     / \\     / \\    ← Developers


        2️⃣ **Scrum Master**
        Facilitador, elimina impedimentos y protege al equipo.

        3️⃣ **Equipo de Desarrollo**
        Miembros multifuncionales que construyen el producto.
        

        """)


    # ---------- VENTANA DETALLADA Product Owner ----------
    def show_po_details(self):
        win = ctk.CTkToplevel(self)
        win.title("Detalles — Product Owner")
        win.geometry("600x500")

        text = ctk.CTkTextbox(
            win, wrap="word",
            font=self.font_text,
            fg_color="#081421",
            text_color="#bdfef0"
        )
        text.pack(fill="both", expand=True, padx=10, pady=10)

        text.insert("1.0",
"""
🧑‍💼 **PRODUCT OWNER (PO)**

El Product Owner es responsable de:

🔹 Maximizar el valor del producto  
🔹 Priorizar el Product Backlog  
🔹 Representar a los interesados  
🔹 Asegurar alineación con la visión del proyecto  

📌 El PO no es jefe del equipo; guía el rumbo del proyecto.

📌 Trabaja de cerca con el alcalde en Neocity, ya que ambos definen prioridades.
"""
        )

    def show_scrum_events(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        📆══════════════════════════════
                EVENTOS DE SCRUM
        ══════════════════════════════📆

        Scrum contiene 5 eventos clave que garantizan el flujo ágil del proyecto.

        1️⃣ **Sprint** — El corazón de Scrum (1–4 semanas).
         Sprint:
        [ PLAN ] → [ DESARROLLAR ] → [ REVISAR ] → [ MEJORAR ]

        2️⃣ **Sprint Planning**
        Se define qué se hará y cómo se hará.

        3️⃣ **Daily Scrum**
        Reunión de 15 minutos.
        Preguntas:
        • ¿Qué hice ayer?  
        • ¿Qué haré hoy?  
        • ¿Qué impedimentos tengo?  

        4️⃣ **Sprint Review**
        Se presenta el incremento del Sprint al PO y stakeholders.

        5️⃣ **Sprint Retrospective**
        Reflexión interna para mejorar procesos y trabajo en equipo.
        """
        )


    def show_scrum_artifacts(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        📦══════════════════════════════
                ARTEFACTOS EN SCRUM
        ══════════════════════════════📦

        1️⃣ **Product Backlog**
        Lista priorizada de TODO lo que se podría desarrollar.

         Backlog:
        ╔══════════════════╗
        ║  PRODUCT BACKLOG ║
        ╠══════════════════╣
        ║ ✔ Historia 1     ║
        ║ ✔ Historia 2     ║
        ║ ✔ Historia 3     ║
        ╚══════════════════╝

        2️⃣ **Sprint Backlog**
        Tareas seleccionadas para el Sprint actual.

        3️⃣ **Incremento**
        Resultado funcional y entregable del Sprint.
        Debe cumplir la **Definition of Done (DoD)**.
        """
        )


    def show_pmbok_intro(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        📙══════════════════════════════
                INTRODUCCIÓN A PMBOK
        ══════════════════════════════📙

        PMBOK es una guía de buenas prácticas para proyectos grandes, complejos y 
        estructurados. Se basa en procesos, documentación y control.

         Project Manager:
                (◕‿◕)
                /|PM|\\
                 / \\

        PMBOK incluye:
        ✔ Procesos de inicio  
        ✔ Planificación detallada  
        ✔ Control de cronograma  
        ✔ Control de costos  
        ✔ Gestión de riesgos  
        ✔ Cierre formal  

        Es ideal para:
        🏗 Construcción  
        🏛 Gobierno  
        🏢 Corporativos  
        ⚙ Proyectos largos  
        """
        )


    def show_pmbok_areas(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        🗂══════════════════════════════
            ÁREAS DE CONOCIMIENTO PMBOK
        ══════════════════════════════🗂

        PMBOK se divide en 10 áreas fundamentales:

        1️⃣ Integración  
        2️⃣ Alcance  
        3️⃣ Cronograma  
        4️⃣ Costos  
        5️⃣ Calidad  
        6️⃣ Recursos  
        7️⃣ Comunicaciones  
        8️⃣ Riesgos  
        9️⃣ Adquisiciones  
        🔟 Interesados  

        Cada área tiene procesos, herramientas y documentos específicos para 
        garantizar control y trazabilidad.
        """
        )


    def show_roles_relation(self):
        self.content.delete("1.0", "end")
        self.content.insert("1.0",
        """
        🏙══════════════════════════════
            RELACIÓN CON ROLES NEOCITY
        ══════════════════════════════🏙

        🟩 **ALCALDE (Similar al Product Owner)**
        :
         \\(^_^)/
            /|\\
            / \\
        • Define prioridades de la ciudad  
        • Maneja interesados  
        • Representa la visión global del proyecto  

        🟦 **INGENIERO URBANO (Scrum Team Técnico + PMBOK Técnico)**
        :
            (^_^)
            /|==|
            / \\
        • Evalúa riesgos, calidad y tiempos  
        • Construye soluciones técnicas  
        • Gestiona cronogramas y recursos  

        🟨 **DIRECTOR ECONÓMICO (PMBOK Costos)**
        :
            (°_°)
            /|\\
            /$\\
        • Control de costos  
        • Adquisiciones y contratos  
        • Viabilidad económica de proyectos  
        """
        )

