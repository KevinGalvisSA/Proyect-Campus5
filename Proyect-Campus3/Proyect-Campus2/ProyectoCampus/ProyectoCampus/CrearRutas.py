import json
import RegresarCoordinacion

def CrearRutasNuevas():
    # Leer el archivo JSON y cargar los datos en una lista de diccionarios
    with open("RutasNuevas.json", "r") as archivo:
        datos = json.load(archivo)
    
    # Extraer la lista de rutas de entrenamiento del primer elemento de la lista
    rutas_de_entrenamiento = datos[0]["rutas_de_entrenamiento"]
    
    # Mostrar las rutas de entrenamiento disponibles
    print("Rutas de entrenamiento disponibles:")
    for idx, ruta in enumerate(rutas_de_entrenamiento, start=1):
        print(f"{idx}. {ruta['nombre']}")
        
    # Solicitar al usuario que ingrese el número de la ruta donde quiere agregar el nuevo curso
    opcion_ruta = int(input("Ingrese el número de la ruta donde desea agregar el nuevo curso: ")) - 1
    
    # Validar la opción de ruta ingresada por el usuario
    if opcion_ruta < 0 or opcion_ruta >= len(rutas_de_entrenamiento):
        print("¡Opción de ruta inválida!")
    else:
        # Obtener la ruta seleccionada
        ruta_seleccionada = rutas_de_entrenamiento[opcion_ruta]
        
        # Solicitar al usuario que ingrese el nombre del nuevo curso
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
        
        # Verificar si el curso ya existe en la lista de cursos de la ruta seleccionada
        if nuevo_curso in ruta_seleccionada["cursos"]:
            print("¡El curso ya está en la lista!")
        else:
            # Agregar el nuevo curso a la lista de cursos de la ruta seleccionada
            ruta_seleccionada["cursos"].append(nuevo_curso)
            
            # Escribir los datos modificados de vuelta al archivo JSON
            with open("RutasNuevas.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
            print("Archivo JSON modificado exitosamente.")
            
    RegresarCoordinacion.regresarMenuC()





