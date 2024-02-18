import json

def CrearRutasNuevas():
    # Leer el archivo JSON y cargar los datos en un diccionario
    with open("RutasNuevas.json", "r") as f:
        datos = json.load(f)
    # Mostrar las rutas de entrenamiento disponibles
    print("Rutas de entrenamiento disponibles:")
    for idx, ruta in enumerate(datos["rutas_de_entrenamiento"], start=1):
        print(f"{idx}. {ruta['nombre']}")
    # Solicitar al usuario que ingrese el número de la ruta donde quiere agregar el nuevo curso
    opcion_ruta = int(input("Ingrese el número de la ruta donde desea agregar el nuevo curso: ")) - 1
    # Validar la opción de ruta ingresada por el usuario
    if opcion_ruta < 0 or opcion_ruta >= len(datos["rutas_de_entrenamiento"]):
        print("¡Opción de ruta inválida!")
    else:
        # Solicitar al usuario que ingrese el nombre del nuevo curso
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
        # Verificar si el curso ya existe en la lista de la ruta seleccionada
        cursos_ruta = datos["rutas_de_entrenamiento"][opcion_ruta]["cursos"]
        if nuevo_curso in cursos_ruta:
            print("¡El curso ya está en la lista!")
        else:
            # Agregar el nuevo curso a la lista de cursos de la ruta seleccionada
            cursos_ruta.append(nuevo_curso)
            # Escribir los datos modificados de vuelta al archivo JSON
            with open("RutasNuevas.json", "w") as f:
                json.dump(datos, f, indent=4)
            print("Archivo JSON modificado exitosamente.")




