from visual import *
from datos import lista
import sys

# Flags
run = True
play_game = False
finish_game = False
score_view = False
correcta = None
contador = 0
puntos = 0
usuario = []

# Primera Pregunta
pregunta = lista[contador]

# Configura el Timer
pygame.time.set_timer(pygame.USEREVENT, 1000)
tiempo_transcurrido = 5

while run:
    lista_eventos = pygame.event.get()

    # Avanzar y Retroceder pj
    if correcta:
        puntos += 10
        pj_x += 90
        rect_pj.x += 90
    elif correcta == False:
        pj_x -= 45
        rect_pj.x -= 45
    
    # Reiniciar tiempo por respuesta y acumular contador
    if correcta or correcta == False:
        tiempo_transcurrido = 5
        contador += 1
        correcta = None

    # Preguntas
    if contador == 16:
        finish_game = True
        correcta = None
    elif tiempo_transcurrido == 0:
        contador += 1
        tiempo_transcurrido = 5
    else:
        pregunta = lista[contador]

    # Colisiones
    if rect_pj.colliderect(rect_avanzar):
        pj_x += 45
        rect_pj.x += 45
    elif rect_pj.colliderect(rect_retroceder):
        pj_x -= 45
        rect_pj.x -= 45
    elif rect_pj.colliderect(rect_utn):
        finish_game = True

    # Evita retroceder pj
    if pj_x < x_inicio and rect_pj.x < x_inicio:
        pj_x = x_inicio
        rect_pj.x = x_inicio

    # Agregar jugador al archivo 
    if len(usuario) == 6:
        data = leer_json("Carrera UTN\\score.json")
        nom = "".join(usuario)
        nuevo_jugador = {"nombre": nom, "puntaje": puntos}
        data['scores'].append(nuevo_jugador)
        escribir_json("Carrera UTN\\score.json", data)
        data = leer_json("Carrera UTN\\score.json")
        usuario = []
        score_view = True

    # Ventanas
    if play_game == False and finish_game == False:
        menu_principal()
    elif play_game and finish_game == False:
        juego(pregunta, pj_x, puntos, tiempo_transcurrido)
    elif finish_game and play_game:
        if score_view:
            puntaje_2(data)
        else:
            puntaje_1(usuario)

    # Eventos
    try:
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.USEREVENT and (play_game == True and finish_game == False):
                if tiempo_transcurrido == 0:
                    finish_game = True
                else:
                    tiempo_transcurrido -= 1
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if play_game == False and finish_game == False:
                        if pulsar_boton(evento, comenzar_x,buttons_y, ancho_boton,alto_boton):
                            play_game = True
                        elif pulsar_boton(evento, terminar_x,buttons_y, ancho_boton,alto_boton):
                            run = False
                    elif play_game and finish_game == False:
                        if pulsar_boton(evento, terminar_x,buttons_y, ancho_boton,alto_boton):
                            finish_game = True
                        if pulsar_boton(evento, 50,resp_y, ancho_resp,alto_resp):
                            correcta = corroborar_correcta(pregunta, "a")
                        elif pulsar_boton(evento, 380,resp_y, ancho_resp,alto_resp):
                            correcta = corroborar_correcta(pregunta, "b")
                        elif pulsar_boton(evento, 690,resp_y, ancho_resp,alto_resp):
                            correcta = corroborar_correcta(pregunta, "c")
                    elif pulsar_boton(evento, salir_x,buttons_y, ancho_boton,alto_boton) and (play_game and finish_game):
                        puntos = 0
                        play_game = False
                        finish_game = False
                        score_view = False
            if evento.type == pygame.KEYDOWN:
                if (evento.key >= pygame.K_a and evento.key <= pygame.K_z) and (play_game and finish_game) and score_view == False:
                    letra = chr(evento.key).upper()
                    usuario.append(letra)
    except Exception as error:
        print(f"ERROR! -> {error}")

    # Reinicio de Flags
    if finish_game:
        contador = 0
        pregunta = lista[contador]
        tiempo_transcurrido = 5
        pj_x = x_inicio
        rect_pj.x = x_inicio

    pygame.display.flip() #Actualiza la ventana por cualquier manipulacion de la misma.
pygame.quit()
sys.exit()