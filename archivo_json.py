import json

def leer_json(archivo_json:str):
    # brief: permite leer un archivo de tipo "JSON".
    # parametros:
    #     archivo_json: el path del archivo JSON.
    # return: lista del archivo JSON
    try:
        with open(archivo_json, "r") as file:
            data = json.load(file)
    except Exception as error:
        print(f"ERROR! -> {error}")

    return data

def escribir_json(nom_archivo:str, data):
    # brief: permite escribir un archivo de tipo "JSON" pasandole la data que quieras guardar.
    # parametros:
    #     archivo_json: el path del archivo JSON.
    #     data: datos o lo que quieras guardar en el archivo.
    # return: -
    try:
        with open(nom_archivo, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as error:
        print(f"ERROR! -> {error}")