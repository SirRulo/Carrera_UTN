from botones import *
from archivo_json import *
from COLORS import *

# Colores
fondo = BLUE
casillas = YELLOW1

# Fuentes Texto
fuente = generar_fuente("Times New Roman",30)
fuente_2 = generar_fuente("Console",45)
fuente_3 = generar_fuente("Impact",40)

# Imagenes
icono = setear_icono("Carrera UTN\\Imagenes\\icono.png")
titulo_1 = escalar_imagen("Carrera UTN\\Imagenes\\titulo.png", 600,500)
titulo_2 = escalar_imagen("Carrera UTN\\Imagenes\\titulo.png", 300,200)
ruta = cargar_imagen("Carrera UTN\\Imagenes\\ruta.png")
utn = cargar_imagen("Carrera UTN\\Imagenes\\utn.png")
timer = escalar_imagen("Carrera UTN\\Imagenes\\timer.png", 50,50)
star = escalar_imagen("Carrera UTN\\Imagenes\\star.png", 50,50)
pj_1 = escalar_imagen("Carrera UTN\\Imagenes\\personaje.png", 25,40)
pj_2 = escalar_imagen("Carrera UTN\\Imagenes\\personaje.png", 150,300)

# Rect Colisiones
rect_pj = pj_1.get_rect()
rect_utn = utn.get_rect()

# Coordenadas del pj y llegada
x_inicio = 111
pj_x = x_inicio
pj_y = 473
rect_pj.x = pj_x
rect_pj.y = pj_y
rect_utn.x = 870
rect_utn.y = ruta_y

# Mostrar Ventanas
def menu_principal():
    # Brief: Muestra el Menu principal del juego llamando a funciones
    PANTALLA.fill(fondo)
    PANTALLA.blit(titulo_1,(210,30))
    PANTALLA.blit(comenzar,(comenzar_x,buttons_y))
    PANTALLA.blit(terminar,(terminar_x,buttons_y))

def juego(dic:dict, pj_x, puntaje, tiempo):
    # Brief: Muestra el Juego y su transcurso llamando a funciones
    # Pregunta y Respuestas
    dibujar_rectangulo(PANTALLA, fondo, 0,0, ANCHO,530)
    dibujar_rectangulo(PANTALLA, GREEN, 0,0, ANCHO,300)
    PANTALLA.blit(rect_a,(50,resp_y))
    PANTALLA.blit(rect_b,(380,resp_y))
    PANTALLA.blit(rect_c,(690,resp_y))
    dibujar_rectangulo(PANTALLA, casillas, 50,resp_y, ancho_resp,alto_resp)
    dibujar_rectangulo(PANTALLA, casillas, 380,resp_y, ancho_resp,alto_resp)
    dibujar_rectangulo(PANTALLA, casillas, 690,resp_y, ancho_resp,alto_resp)
    mostrar_texto(fuente, PANTALLA, dic["pregunta"], WHITE, 180,80)
    mostrar_texto(fuente, PANTALLA, dic["a"], BLACK, 60,200)
    mostrar_texto(fuente, PANTALLA, dic["b"], BLACK, 390,200)
    mostrar_texto(fuente, PANTALLA, dic["c"], BLACK, 700,200)
    # Puntaje y Tiempo
    PANTALLA.blit(star,(310,370))
    PANTALLA.blit(timer,(610,370))
    mostrar_texto(fuente, PANTALLA, f"{puntaje}", WHITE, 376,379)
    mostrar_texto(fuente, PANTALLA, f"{tiempo}", WHITE, 668,379)
    # Ruta y Personaje
    pygame.draw.rect(PANTALLA, BLACK, rect_avanzar)
    pygame.draw.rect(PANTALLA, BLACK, rect_retroceder)
    pygame.draw.rect(PANTALLA, BLACK, rect_pj)
    pygame.draw.rect(PANTALLA, BLACK, rect_utn)
    PANTALLA.blit(ruta,(150,ruta_y))
    PANTALLA.blit(utn,(870,ruta_y))
    PANTALLA.blit(pj_1,(pj_x,473))

def puntaje_1(usuario:list):
    # Brief: Muestra imagenes y realiza la muestra del nombre ingresado para luego mostrar el puntaje llamando a funciones.
    # Parametros: usuario: lista que contiene cada letra del jugador ingresado.
    PANTALLA.fill(fondo)
    PANTALLA.blit(titulo_2,(650,40))
    PANTALLA.blit(pj_2,(700,260))
    PANTALLA.blit(salir,(salir_x,buttons_y))
    mostrar_texto(fuente_2, PANTALLA, "PUNTAJE", WHITE, 150,30)
    nom = "".join(usuario)
    mostrar_texto(fuente_2, PANTALLA, nom, WHITE, 130,100)

def puntaje_2(data):
    # Brief: Muestra el listado de puntajes y nombres ordenados llamando a funciones.
    # Parametros: data: la data representa el archivo sobreescrito con el nuevo jugador guardado.
    y = 100
    dibujar_rectangulo(PANTALLA, fondo, 120,95, 260,600)
    jugadores = data["scores"]
    jugadores.sort(key=lambda jugador: jugador["puntaje"], reverse=True)
    for e in jugadores[:10]:
        mostrar_texto(fuente, PANTALLA, e["nombre"], WHITE, 130,y)
        mostrar_texto(fuente, PANTALLA, f"{e["puntaje"]}", WHITE, 330,y)
        y += 50