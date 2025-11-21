import sys
import pygame
import random

preguntas_por_rol = {
    "Alcalde": [
        {
            "pregunta": "Durante una crisis en la ciudad, ¿qué harías primero según los principios de gestión de proyectos?",
            "opciones": [
                "Reunir al equipo para priorizar tareas y asignar responsables.",
                "Esperar a tener toda la información antes de actuar.",
                "Delegar todo sin comunicarte con el equipo."
            ],
            "respuesta_correcta": "Reunir al equipo para priorizar tareas y asignar responsables.",
            "explicacion": "Refleja la priorización y colaboración inmediata: convoca al equipo, identifica críticos y asigna responsables.",
            "puntos": 10
        },
        {
            "pregunta": "La ciudad enfrenta un apagón masivo. ¿Cuál es tu primera acción como líder?",
            "opciones": [
                "Convocar al equipo clave y priorizar las áreas críticas.",
                "Esperar a que los técnicos te envíen un informe completo.",
                "Culpar al departamento de energía."
            ],
            "respuesta_correcta": "Convocar al equipo clave y priorizar las áreas críticas.",
            "explicacion": "Refleja la priorización y colaboración inmediata del Scrum ante problemas.",
            "puntos": 10
        },
        {
            "pregunta": "Un proyecto de transporte público está retrasado. ¿Qué harías?",
            "opciones": [
                "Analizar impedimentos y pedir al equipo alternativas.",
                "Presionar para acelerar sin plan.",
                "Ignorar el retraso."
            ],
            "respuesta_correcta": "Analizar impedimentos y pedir al equipo alternativas.",
            "explicacion": "La gestión de impedimentos es clave del Scrum Master.",
            "puntos": 10
        },
        {
            "pregunta": "Los ciudadanos piden más transparencia. ¿Qué harías?",
            "opciones": [
                "Publicar avances del proyecto como en un burndown chart.",
                "Esperar al informe final.",
                "Delegar la comunicación sin supervisión."
            ],
            "respuesta_correcta": "Publicar avances del proyecto como en un burndown chart.",
            "explicacion": "La transparencia es un valor central de Scrum.",
            "puntos": 10
        },
        {
            "pregunta": "Necesitas aprobar un presupuesto para un nuevo parque. ¿Qué haces?",
            "opciones": [
                "Revisas alcance, riesgos y costos antes de autorizar.",
                "Lo apruebas rápido para no atrasar.",
                "Lo rechazas por precaución."
            ],
            "respuesta_correcta": "Revisas alcance, riesgos y costos antes de autorizar.",
            "explicacion": "En PMBOK se evalúa el triángulo de alcance-tiempo-costo.",
            "puntos": 10
        },
        {
            "pregunta": "Tu equipo trabaja lento por sobrecarga. ¿Qué haces?",
            "opciones": [
                "Revisas la capacidad del sprint y reduces tareas.",
                "Los presionas a trabajar horas extra.",
                "Ignoras la situación."
            ],
            "respuesta_correcta": "Revisas la capacidad del sprint y reduces tareas.",
            "explicacion": "Scrum recomienda capacidad realista según velocidad del equipo.",
            "puntos": 10
        },
        {
            "pregunta": "Existen quejas de falta de coordinación entre áreas. ¿Qué haces?",
            "opciones": [
                "Organizar una reunión diaria corta entre líderes.",
                "Enviar un comunicado distante.",
                "Asignar responsabilidades sin escuchar a nadie."
            ],
            "respuesta_correcta": "Organizar una reunión diaria corta entre líderes.",
            "explicacion": "Simula la Daily Scrum: comunicación rápida y efectiva.",
            "puntos": 10
        },
        {
            "pregunta": "Un distrito tiene problemas recurrentes. ¿Qué haces?",
            "opciones": [
                "Analizar causa raíz usando lecciones aprendidas.",
                "Poner un parche temporal.",
                "Pedir más reportes y no actuar."
            ],
            "respuesta_correcta": "Analizar causa raíz usando lecciones aprendidas.",
            "explicacion": "PMBOK sugiere revisar lecciones aprendidas para evitar retrabajo.",
            "puntos": 10
        },
        {
            "pregunta": "Hay presión política para acelerar un proyecto. ¿Qué haces?",
            "opciones": [
                "Evaluar impacto en alcance y comunicar riesgos.",
                "Aceptar sin analizar.",
                "Ignorar la presión y no comunicar nada."
            ],
            "respuesta_correcta": "Evaluar impacto en alcance y comunicar riesgos.",
            "explicacion": "En PMBOK el control de cambios es esencial.",
            "puntos": 10
        },
        {
            "pregunta": "Tu equipo propone una idea innovadora para movilidad. ¿Qué haces?",
            "opciones": [
                "Evaluas el valor y factibilidad antes de decidir.",
                "La ignoras por ser diferente.",
                "La rechazas por riesgo."
            ],
            "respuesta_correcta": "Evaluas el valor y factibilidad antes de decidir.",
            "explicacion": "Scrum promueve inspección, adaptación y mejora continua.",
            "puntos": 10
        },
        {
            "pregunta": "Debes priorizar proyectos urbanos. ¿Qué criterio usas?",
            "opciones": [
                "Priorizas valor para la ciudadanía.",
                "Priorizas lo que genera menos trabajo.",
                "Priorizas según presión política."
            ],
            "respuesta_correcta": "Priorizas valor para la ciudadanía.",
            "explicacion": "Como Product Owner, se prioriza por valor entregado.",
            "puntos": 10
        },
    ],

    "Ingeniero Urbano": [
    {
        "pregunta": "El diseño de un puente presenta inconsistencias. ¿Qué haces?",
        "opciones": [
            "Reportas el impedimento y buscas una solución colaborativa.",
            "Lo ignoras mientras no falle.",
            "Culpas a otro departamento."
        ],
        "respuesta_correcta": "Reportas el impedimento y buscas una solución colaborativa.",
        "explicacion": "Scrum enfatiza eliminar impedimentos rápidamente.",
        "puntos": 10
    },
    {
        "pregunta": "Una obra está detenida por falta de materiales. ¿Qué haces?",
        "opciones": [
            "Comunicarse con el Product Owner para replanificar.",
            "Esperar sin actuar.",
            "Forzar a los trabajadores a continuar."
        ],
        "respuesta_correcta": "Comunicarse con el Product Owner para replanificar.",
        "explicacion": "En PMBOK se maneja el control de recursos.",
        "puntos": 10
    },
    {
        "pregunta": "Un técnico propone un rediseño más eficiente. ¿Qué haces?",
        "opciones": [
            "Lo analizas porque podría aportar valor.",
            "Lo descartas por no estar en el plan.",
            "Lo pospones sin evaluarlo."
        ],
        "respuesta_correcta": "Lo analizas porque podría aportar valor.",
        "explicacion": "Scrum favorece la mejora continua y participación.",
        "puntos": 10
    },
    {
        "pregunta": "Notas riesgo de inundación en una zona urbanizada. ¿Qué haces?",
        "opciones": [
            "Agregas el riesgo al registro y analizas respuestas.",
            "Lo ignoras por ahora.",
            "Esperas a que la lluvia confirme."
        ],
        "respuesta_correcta": "Agregas el riesgo al registro y analizas respuestas.",
        "explicacion": "En PMBOK se maneja un registro de riesgos.",
        "puntos": 10
    },
    {
        "pregunta": "El equipo está desmotivado. ¿Qué haces?",
        "opciones": [
            "Hacer una retrospectiva para identificar mejoras.",
            "Ignorar el problema.",
            "Aumentar presión."
        ],
        "respuesta_correcta": "Hacer una retrospectiva para identificar mejoras.",
        "explicacion": "Scrum usa retrospectivas para mejorar continuamente.",
        "puntos": 10
    },
    {
        "pregunta": "El plano de drenaje presenta conflicto de tuberías. ¿Qué haces?",
        "opciones": [
            "Coordinar una revisión inmediata con los involucrados.",
            "Seguir con el diseño incorrecto.",
            "Culpar al proveedor."
        ],
        "respuesta_correcta": "Coordinar una revisión inmediata con los involucrados.",
        "explicacion": "Scrum busca resolver problemas colaborativamente.",
        "puntos": 10
    },
    {
        "pregunta": "Un ciudadano reporta un posible peligro estructural. ¿Qué haces?",
        "opciones": [
            "Lo evalúas rápido y priorizas si es crítico.",
            "Esperas a que llegue más evidencia.",
            "Lo ignoras hasta que haya inspección completa."
        ],
        "respuesta_correcta": "Lo evalúas rápido y priorizas si es crítico.",
        "explicacion": "Scrum prioriza según valor y urgencia.",
        "puntos": 10
    },
    {
        "pregunta": "Necesitas actualizar un plano pero el equipo está saturado. ¿Qué haces?",
        "opciones": [
            "Revisas la carga del sprint y reasignas tareas.",
            "Los obligas a hacerlo sin descanso.",
            "Pospones indefinidamente."
        ],
        "respuesta_correcta": "Revisas la carga del sprint y reasignas tareas.",
        "explicacion": "Scrum ajusta capacidad según velocidad del equipo.",
        "puntos": 10
    },
    {
        "pregunta": "Un error podría generar sobrecosto. ¿Qué haces?",
        "opciones": [
            "Registrar el riesgo y tomar acciones preventivas.",
            "No decir nada para no alarmar.",
            "Esperar al cierre del proyecto."
        ],
        "respuesta_correcta": "Registrar el riesgo y tomar acciones preventivas.",
        "explicacion": "PMBOK destaca la prevención sobre la corrección.",
        "puntos": 10
    },
    {
        "pregunta": "Debes entregar un informe técnico. ¿Qué enfoque usas?",
        "opciones": [
            "Presentar datos actuales en forma transparente.",
            "Ajustar números para que se vea bien.",
            "Reducir información para ahorrar tiempo."
        ],
        "respuesta_correcta": "Presentar datos actuales en forma transparente.",
        "explicacion": "La transparencia es un valor fundamental de Scrum.",
        "puntos": 10
    },
    ],

    "Director Económico": [
    {
        "pregunta": "El gasto mensual subió inesperadamente. ¿Qué haces?",
        "opciones": [
            "Revisas las causas y ajustas presupuesto.",
            "Ignoras el incremento.",
            "Culpas al área operativa."
        ],
        "respuesta_correcta": "Revisas las causas y ajustas presupuesto.",
        "explicacion": "PMBOK exige control de costos continuo.",
        "puntos": 10
    },
    {
        "pregunta": "El equipo propone cambiar de software financiero. ¿Qué haces?",
        "opciones": [
            "Analizas costo-beneficio antes de decidir.",
            "Lo rechazas sin estudio.",
            "Lo apruebas sin evaluación."
        ],
        "respuesta_correcta": "Analizas costo-beneficio antes de decidir.",
        "explicacion": "La evaluación de cambios es parte del control integrado en PMBOK.",
        "puntos": 10
    },
    {
        "pregunta": "Una inversión tiene riesgo alto. ¿Qué haces?",
        "opciones": [
            "Analizas riesgos y defines respuesta.",
            "La ignoras.",
            "La aceptas sin pensar."
        ],
        "respuesta_correcta": "Analizas riesgos y defines respuesta.",
        "explicacion": "Gestión de riesgos: identificar, analizar y planear.",
        "puntos": 10
    },
    {
        "pregunta": "El cronograma depende de la aprobación de presupuesto. ¿Qué haces?",
        "opciones": [
            "Revisas impacto y actualizas cronograma.",
            "No haces nada hasta el final.",
            "Aceleras sin analizar."
        ],
        "respuesta_correcta": "Revisas impacto y actualizas cronograma.",
        "explicacion": "PMBOK: gestionar línea base de cronograma.",
        "puntos": 10
    },
    {
        "pregunta": "Hay retrasos por falta de recursos económicos. ¿Qué haces?",
        "opciones": [
            "Replanificas con stakeholders según disponibilidad.",
            "Presionas sin recursos.",
            "Ignoras la situación."
        ],
        "respuesta_correcta": "Replanificas con stakeholders según disponibilidad.",
        "explicacion": "Control de recursos y comunicación efectiva.",
        "puntos": 10
    },
    {
        "pregunta": "Un proyecto no justifica sus beneficios. ¿Qué haces?",
        "opciones": [
            "Revisar el caso de negocio y ajustar alcance.",
            "Seguir adelante sin cuestionar.",
            "Cancelar sin analizar."
        ],
        "respuesta_correcta": "Revisar el caso de negocio y ajustar alcance.",
        "explicacion": "PMBOK exige validar beneficios y valor.",
        "puntos": 10
    },
    {
        "pregunta": "El equipo no entiende los costos del proyecto. ¿Qué haces?",
        "opciones": [
            "Explicar y compartir información relevante.",
            "Decir que no es su asunto.",
            "Ignorar el problema."
        ],
        "respuesta_correcta": "Explicar y compartir información relevante.",
        "explicacion": "Scrum promueve transparencia total.",
        "puntos": 10
    },
    {
        "pregunta": "Un proveedor aumenta precios. ¿Qué haces?",
        "opciones": [
            "Revisas contratos y evalúas alternativas.",
            "Aceptas sin negociar.",
            "Culpas al proveedor."
        ],
        "respuesta_correcta": "Revisas contratos y evalúas alternativas.",
        "explicacion": "Gestión de adquisiciones en PMBOK.",
        "puntos": 10
    },
    {
        "pregunta": "Detectas gastos duplicados. ¿Qué haces?",
        "opciones": [
            "Corregir y actualizar informes.",
            "No decir nada.",
            "Esconder el error."
        ],
        "respuesta_correcta": "Corregir y actualizar informes.",
        "explicacion": "PMBOK promueve exactitud y control de documentos.",
        "puntos": 10
    },
    {
        "pregunta": "Debes priorizar inversiones para el siguiente año. ¿Qué haces?",
        "opciones": [
            "Priorizas según valor y retorno esperado.",
            "Priorizas al azar.",
            "Priorizas lo más barato."
        ],
        "respuesta_correcta": "Priorizas según valor y retorno esperado.",
        "explicacion": "Scrum y PMBOK priorizan por valor entregado.",
        "puntos": 10
    },
    ]
}


def wrap_text(text, max_width, font):
    words = text.split()
    lines = []
    cur = []
    for w in words:
        cur.append(w)
        test = " ".join(cur)
        if font.size(test)[0] > max_width:
            # retirar última palabra y cerrar línea
            cur.pop()
            if cur:
                lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def main(argv):
    user = argv[1] if len(argv) > 1 else "Jugador"
    role = argv[2] if len(argv) > 2 else "Alcalde"

    pygame.init()
    WIDTH, HEIGHT = 1224, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neocity - Quiz")
    clock = pygame.time.Clock()
    random.seed()

    # Background (fallback simple grid)
    try:
        bg = pygame.image.load("background_map.jpg").convert()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    except Exception:
        bg = pygame.Surface((WIDTH, HEIGHT))
        bg.fill((6, 12, 20))
        # simple grid
        for x in range(0, WIDTH, 80):
            pygame.draw.line(bg, (8, 18, 30), (x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, 80):
            pygame.draw.line(bg, (8, 18, 30), (0,y),(WIDTH,y))

    # Colors
    NEON = (0, 255, 218)
    ACCENT = (44, 170, 150)
    TEXT = (220, 250, 245)
    SCORE_COLOR = (255, 215, 100)
    CORRECT_COLOR = (0, 220, 120)
    WRONG_COLOR = (255, 110, 110)
    BOX_BG = (12, 24, 34)
    HOVER_BG = (18, 34, 46)

    # Fonts
    title_font = pygame.font.Font(None, 47)
    header_font = pygame.font.Font(None, 40)
    info_font = pygame.font.Font(None, 25)
    small_font = pygame.font.Font(None, 20)

    # Game state
    score = 0
    current_question_index = 0
    questions = preguntas_por_rol.get(role, [])
    shuffled_for_index = {}   # store shuffled options per question index
    option_rects = []         # rects for click detection for current question

    # Explanation state
    show_explanation = False
    selected_answer = ""
    is_correct = False
    explanation_text = ""

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        mouse_pressed = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                mouse_pressed = True
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
                elif show_explanation and ev.key == pygame.K_SPACE:
                    # go next question
                    show_explanation = False
                    selected_answer = ""
                    is_correct = False
                    explanation_text = ""
                    current_question_index += 1
                    option_rects = []
                elif not show_explanation:
                    # keyboard selection 1/2/3
                    mapping = {pygame.K_1:0, pygame.K_2:1, pygame.K_3:2, pygame.K_KP1:0, pygame.K_KP2:1, pygame.K_KP3:2}
                    if ev.key in mapping and current_question_index < len(questions):
                        idx = mapping[ev.key]
                        opts = shuffled_for_index.get(current_question_index)
                        if opts and idx < len(opts):
                            selected_answer = opts[idx]
                            q = questions[current_question_index]
                            is_correct = (selected_answer == q["respuesta_correcta"])
                            if is_correct:
                                score += q.get("puntos", 0)
                            explanation_text = q.get("explicacion","")
                            show_explanation = True

        # Render background
        screen.blit(bg, (0,0))

        # Neon top bar
        pygame.draw.rect(screen, BOX_BG, (40,20, WIDTH-80, 80), border_radius=12)
        pygame.draw.rect(screen, NEON, (36,16, WIDTH-72, 88), 2, border_radius=14)
        title = title_font.render("NEOCITY — Cuestionario", True, NEON)
        screen.blit(title, (60, 30))
        user_txt = small_font.render(f"{user}  •  Rol: {role}", True, TEXT)
        screen.blit(user_txt, (WIDTH-320, 40))

        # Score box
        score_txt = header_font.render(f"SCORE: {score}", True, SCORE_COLOR)
        score_rect = score_txt.get_rect(topright=(WIDTH-60, 110))
        screen.blit(score_txt, score_rect)

        # Main panel
        panel_x, panel_y = 60, 130
        panel_w, panel_h = WIDTH - 120, HEIGHT - 200
        panel_rect = pygame.Rect(panel_x, panel_y, panel_w, panel_h)
        s = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        s.fill((6, 12, 20, 180))
        screen.blit(s, (panel_x, panel_y))
        pygame.draw.rect(screen, NEON, (panel_x-2, panel_y-2, panel_w+4, panel_h+4), 2, border_radius=14)

        if current_question_index < len(questions):
            q = questions[current_question_index]

            # Ensure shuffled options exist for this question index
            if current_question_index not in shuffled_for_index:
                opts = q["opciones"][:]
                random.shuffle(opts)
                shuffled_for_index[current_question_index] = opts

            opts = shuffled_for_index[current_question_index]

            # Question title and box (wider)
            q_title = header_font.render(f"Pregunta {current_question_index+1} / {len(questions)}", True, ACCENT)
            screen.blit(q_title, (panel_x+24, panel_y+18))

            # Question box
            qbox_rect = pygame.Rect(panel_x+24, panel_y+68, panel_w-48, 160)
            pygame.draw.rect(screen, BOX_BG, qbox_rect, border_radius=10)
            pygame.draw.rect(screen, ACCENT, qbox_rect, 2, border_radius=10)

            # Render wrapped question text (wider)
            lines = wrap_text(q["pregunta"], qbox_rect.width-40, info_font)
            for i, line in enumerate(lines):
                screen.blit(info_font.render(line, True, TEXT), (qbox_rect.x+20, qbox_rect.y+18 + i*32))

            # Options area - make them big and interactive
            option_rects = []
            for i, opt in enumerate(opts):
                oy = qbox_rect.y + 200 + i * 110
                orect = pygame.Rect(panel_x+24, oy, panel_w-48, 96)
                hovered = orect.collidepoint(mx,my)
                color_bg = HOVER_BG if hovered else BOX_BG
                pygame.draw.rect(screen, color_bg, orect, border_radius=12)
                pygame.draw.rect(screen, ACCENT if hovered else (28,48,60), orect, 2, border_radius=12)

                # option number circle
                circle_center = (orect.x+46, orect.y+48)
                pygame.draw.circle(screen, NEON if hovered else ACCENT, circle_center, 18)
                num_surf = header_font.render(str(i+1), True, (6, 12, 20))
                ns = num_surf.get_rect(center=circle_center)
                screen.blit(num_surf, ns)

                # option text wrapped
                opt_lines = wrap_text(opt, orect.width-140, info_font)
                for j, ol in enumerate(opt_lines):
                    screen.blit(info_font.render(ol, True, TEXT), (orect.x+110, orect.y+20 + j*28))

                option_rects.append(orect)

            # Mouse click handling (outside event loop because we need rects)
            if mouse_pressed and not show_explanation:
                for idx, rect in enumerate(option_rects):
                    if rect.collidepoint(mx,my):
                        selected_answer = opts[idx]
                        is_correct = (selected_answer == q["respuesta_correcta"])
                        if is_correct:
                            score += q.get("puntos",0)
                        explanation_text = q.get("explicacion","")
                        show_explanation = True
                        break

            # Instructions
            inst = small_font.render("", True, (180,220,215))
            screen.blit(inst, (panel_x+24, panel_y+panel_h-40))

        else:
            # Result screen
            rx, ry, rw, rh = panel_x+120, panel_y+60, panel_w-240, panel_h-160
            pygame.draw.rect(screen, BOX_BG, (rx, ry, rw, rh), border_radius=14)
            pygame.draw.rect(screen, NEON, (rx-3, ry-3, rw+6, rh+6), 2, border_radius=16)

            fin = title_font.render("¡Cuestionario Completado!", True, NEON)
            screen.blit(fin, (WIDTH//2 - fin.get_width()//2, ry+24))
            max_score = len(questions) * 10 if questions else 0
            score_surf = header_font.render(f"Puntuación final: {score} / {max_score}", True, SCORE_COLOR)
            screen.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, ry+110))
            perc = (score / max_score * 100) if max_score else 0.0
            perc_surf = info_font.render(f"{perc:.1f}% correcto", True, ACCENT)
            screen.blit(perc_surf, (WIDTH//2 - perc_surf.get_width()//2, ry+170))
            note = small_font.render("Pulsa ESC para salir", True, (180,220,215))
            screen.blit(note, (WIDTH//2 - note.get_width()//2, ry+240))

        # Explanation overlay when active
        if show_explanation:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((6,8,12,180))
            screen.blit(overlay, (0,0))

            box_w, box_h = WIDTH-240, 420
            bx, by = 120, HEIGHT//2 - box_h//2
            pygame.draw.rect(screen, BOX_BG, (bx,by,box_w,box_h), border_radius=14)
            pygame.draw.rect(screen, NEON, (bx-3,by-3,box_w+6,box_h+6), 2, border_radius=16)

            # Title correct/incorrect
            header_txt = "RESPUESTA CORRECTA" if is_correct else "RESPUESTA INCORRECTA"
            header_col = CORRECT_COLOR if is_correct else WRONG_COLOR
            header_s = header_font.render(header_txt, True, header_col)
            screen.blit(header_s, (bx + 30, by + 20))

            # Your answer
            ya = small_font.render("Tu respuesta:", True, ACCENT)
            screen.blit(ya, (bx+30, by+80))
            ya_lines = wrap_text(f"• {selected_answer}", box_w-140, small_font)
            for i,l in enumerate(ya_lines):
                screen.blit(small_font.render(l, True, TEXT), (bx+50, by+110 + i*24))

            # Correct answer
            ca = small_font.render("Respuesta correcta:", True, CORRECT_COLOR)
            screen.blit(ca, (bx+30, by+180))
            ca_lines = wrap_text(f"• {questions[current_question_index]['respuesta_correcta']}", box_w-140, small_font)
            for i,l in enumerate(ca_lines):
                screen.blit(small_font.render(l, True, CORRECT_COLOR), (bx+50, by+210 + i*24))

            # Explanation
            ex = small_font.render("Explicación:", True, NEON)
            screen.blit(ex, (bx+30, by+270))
            ex_lines = wrap_text(explanation_text, box_w-140, small_font)
            for i,l in enumerate(ex_lines):
                screen.blit(small_font.render(l, True, TEXT), (bx+50, by+300 + i*22))

            cont = small_font.render("Pulsa ESPACIO para continuar", True, (200,240,230))
            screen.blit(cont, (bx + box_w//2 - cont.get_width()//2, by + box_h - 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))