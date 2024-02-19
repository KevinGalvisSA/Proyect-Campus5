import json
import Coordinacion
def asignacionCampers():
    # Cargar la información de los campers y la configuración desde el archivo JSON
    with open('Campers.json', 'r') as archivo_campers, open('Areas.json', 'r') as archivo_areas:
        campers = json.load(archivo_campers)
        Areas = json.load(archivo_areas)
        rutas = Areas["rutas"]
        areas_entrenamiento = Areas["areas_entrenamiento"]

    # Solicitar al usuario el documento del camper
    documento_camper = input("Ingrese el documento del camper: ")

    # Verificar si el documento ingresado existe en los campers
    if documento_camper in campers:
        # Obtener la información del camper
        datos_camper = campers[documento_camper]

        print("\nOpciones de Área de Entrenamiento y Ruta de Entrenamiento:")
        for area, info_area in areas_entrenamiento.items():
            print(f"\nÁrea de Entrenamiento: {area}")
            for i, ruta in enumerate(rutas, start=1):
                print(f"  {i}. Ruta {ruta}")

        opcion_area = input("\nSeleccione el área de entrenamiento (sputnik, artemis, apolo): ")
        opcion_ruta = input("Seleccione la ruta de entrenamiento (1-3): ")

        if opcion_area in areas_entrenamiento and opcion_ruta.isdigit() and 1 <= int(opcion_ruta) <= len(rutas):
            area_seleccionada = opcion_area
            ruta_seleccionada = rutas[int(opcion_ruta) - 1]

            areas_entrenamiento[area_seleccionada]['campers_asignados'].append({
                'id': documento_camper,
                'nombre': datos_camper['nombre'],
                'ruta_entrenamiento': ruta_seleccionada
            })

            # Guardar la información actualizada en el archivo JSON
            with open('Areas.json', 'w') as archivo_areas:
                json.dump(Areas, archivo_areas, indent=4)

            print("\nEl camper ha sido asignado exitosamente:")
            print(f"- Camper: {datos_camper['nombre']}")
            print(f"- Área de Entrenamiento: {area_seleccionada}")
            print(f"- Ruta de Entrenamiento: {ruta_seleccionada}")

        else:
            print("Opción de área o ruta inválida.")

    else:
        print("El documento del camper no se encontró en el registro.")

def asignacionTrainers():
    # Cargar la información de los campers y la configuración desde el archivo JSON
    with open('Trainers.json', 'r') as archivo_trainers, open('Areas.json', 'r') as archivo_areas:
        trainers = json.load(archivo_trainers)
        Areas = json.load(archivo_areas)
        rutas = Areas["rutas"]
        areas_entrenamiento = Areas["areas_entrenamiento"]

    # Solicitar al usuario el documento del camper
    documento_trainer = input("Ingrese el documento del trainer: ")

    # Verificar si el documento ingresado existe en los trainers
    if documento_trainer in trainers:
        # Obtener la información del trainer
        datos_trainer = trainers[documento_trainer]

        print("\nOpciones de Área de Entrenamiento y Ruta de Entrenamiento:")
        for area, info_area in areas_entrenamiento.items():
            print(f"\nÁrea de Entrenamiento: {area}")
            for i, ruta in enumerate(rutas, start=1):
                print(f"  {i}. Ruta {ruta}")

        opcion_area = input("\nSeleccione el área de entrenamiento (sputnik, artemis, apolo): ")
        opcion_ruta = input("Seleccione la ruta de entrenamiento (1-3): ")

        if opcion_area in areas_entrenamiento and opcion_ruta.isdigit() and 1 <= int(opcion_ruta) <= len(rutas):
            area_seleccionada = opcion_area
            ruta_seleccionada = rutas[int(opcion_ruta) - 1]

            areas_entrenamiento[area_seleccionada]['trainers_asignados'].append({
                'id': documento_trainer,
                'nombre': datos_trainer['nombre'],
                'ruta_entrenamiento': ruta_seleccionada
            })

            # Guardar la información actualizada en el archivo JSON
            with open('Areas.json', 'w') as archivo_areas:
                json.dump(Areas, archivo_areas, indent=4)

            print("\nEl trainer ha sido asignado exitosamente:")
            print(f"- Trainer: {datos_trainer['nombre']}")
            print(f"- Área de Entrenamiento: {area_seleccionada}")
            print(f"- Ruta de Entrenamiento: {ruta_seleccionada}")

        else:
            print("Opción de área o ruta inválida.")

    else:
        print("El documento del Trainer no se encontró en el registro.")

def TerminarMenuAsignacion():
    print("Entendido. Saliendo del 'MENU ASIGNACION'...")
    print("")
    print("Solicitud completada")
    print("")
    print("Hasta Luego!")
    Coordinacion.MenuCoordinacion2()


def MenuAsignacion():
    while True:
        try:
            print("********************************************")
            print("**             MENÚ ASIGNACION            **")
            print("********************************************")
            print("** 1 -> Asignar Camper                    **")
            print("** 2 -> Asginar Trainer                   **")
            print("** 3 -> Salir                             **")
            print("********************************************")

            opc = int(input("Digite el identificador de la opcion a la cual desea acceder: "))

            if opc == 1:
                asignacionCampers()
            elif opc == 2:
                asignacionTrainers()
            elif opc == 3:
                TerminarMenuAsignacion()
        except Exception:
            print("Ha ocurrido un error")
            print("Probablemente ingresaste una variable que no es del tipo 'int'. Asegurate de digitar uno de los identificadores (1, 2, 3).")

MenuAsignacion()