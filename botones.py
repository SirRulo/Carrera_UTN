from imagen import *

# Medidas Botones
ancho_boton = 250
alto_boton = 100
ancho_resp = 260
alto_resp = 50

# Coordenadas
comenzar_x = 161
terminar_x = 604
salir_x = 700
buttons_y = 600
resp_y = 190
ruta_y = 480

def generar_superficie(ancho, alto):
    # brief: genera una superficie con sus medidas.
    # parametros:
    #     ancho: medida del ancho de la superficie que se genera.
    #     alto: medida del alto de la superficie que se genera.
    # return: una superficie
    return pygame.Surface((ancho, alto))

def convertir_boton(archivo_imagen:str, ancho, alto):
    # brief: genera y escala por un path de imagen, un boton con superficie.
    # parametros:
    #     ancho: medida del ancho del boton que se genera.
    #     alto: medida del alto del boton que se genera.
    # return: boton
    boton = generar_superficie(ancho,alto)
    boton = escalar_imagen(archivo_imagen, ancho, alto)
    return boton

def pulsar_boton(event, x,y, ancho,alto):
    # brief: permite determinar el rango de un boton por su ancho y alto, asi poder presionarlo.
    # parametros:
    #     event: la lista de eventos.
    #     x,y: las coordenadas del boton.
    #     ancho,alto: el rango de medida del boton
    # return: True
    if x < event.pos[0] < x + ancho and y < event.pos[1] < y + alto:
        return True

# Crear Botones
comenzar = convertir_boton("Carrera UTN\\Imagenes\\comenzar.png", ancho_boton,alto_boton)
terminar = convertir_boton("Carrera UTN\\Imagenes\\terminar.png", ancho_boton,alto_boton)
salir = convertir_boton("Carrera UTN\\Imagenes\\salir.png", ancho_boton,alto_boton)
rect_a = generar_superficie(ancho_resp,alto_resp)
rect_b = generar_superficie(ancho_resp,alto_resp)
rect_c = generar_superficie(ancho_resp,alto_resp)

# Colisiones
ancho_col = 40
alto_col = 30
avanzar = generar_superficie(ancho_col,alto_col)
retroceder = generar_superficie(ancho_col,alto_col)
rect_avanzar = avanzar.get_rect()
rect_retroceder = retroceder.get_rect()


# Coordenadas Colosiones
rect_avanzar.x = 375
rect_avanzar.y = ruta_y
rect_retroceder.x = 643
rect_retroceder.y = ruta_y