import json
import RegresarCoordinacion

def cargar_trainers():
    with open('Trainers.json', 'r') as archivo:
        trainers = json.load(archivo)
    return trainers

def crearHorariosTrainers(trainers):
    horariosTrainer = {}
    for documento, trainerData in trainers.items():
        rutas = trainerData.get("rutas", [])
        horariosTrainer[documento] = {}
        horarioElegido = input("Ingrese el horario para el Trainer. (1 para 6:00 - 14:00, 2 para 14:00 - 22:00): ")
        if horarioElegido == "1":
            horariosTrainer[documento]["6:00 - 14:00"] = {ruta: False for ruta in rutas}
            horariosTrainer[documento]["14:00 - 22:00"] = {}
        elif horarioElegido == "2":
            horariosTrainer[documento]["6:00 - 14:00"] = {}
            horariosTrainer[documento]["14:00 - 22:00"] = {ruta: False for ruta in rutas}
        else:
            print("Opción no válida. Se asignará el horario 1 por defecto.")
            horariosTrainer[documento]["6:00 - 14:00"] = {ruta: False for ruta in rutas}
            horariosTrainer[documento]["14:00 - 22:00"] = {}
    return horariosTrainer


def puede_dirigir_trainer(documento, ruta, horariosTrainer):
    return horariosTrainer.get(documento, {}).get(ruta, False)

def añadirHorarios():
# Cargar los datos de los Trainers desde el archivo JSON
    trainers = cargar_trainers()

    # Crear los horarios de los Trainers
    horariosTrainer = crearHorariosTrainers(trainers)

    # Solicitar al usuario que ingrese el documento del Trainer y la ruta que desea verificar
    documento = input("Ingrese el documento del Trainer: ")
    ruta = input("Ingrese la ruta que desea verificar: ")

    # Verificar si el Trainer puede dirigir la ruta especificada
    if documento not in trainers:
        print("El documento ingresado no está registrado.")
    else:
        if puede_dirigir_trainer(documento, ruta, horariosTrainer):
            print(f"El Trainer {documento} puede dirigir la ruta {ruta}")
        else:
            print(f"El Trainer {documento} no puede dirigir la ruta {ruta}")

        # Solicitar al usuario si desea permitir que el Trainer dirija la ruta especificada
        decision = input("¿Desea permitir que el Trainer dirija esta ruta? (sí/no): ").lower()
        if decision == "s" or decision == "si":
            horariosTrainer[documento][ruta] = True
            print(f"Se ha permitido que el Trainer {documento} dirija la ruta {ruta}")
        elif decision == "n" or decision == "no":
            print(f"No se permite que el Trainer {documento} dirija la ruta {ruta}")
        else:
            print("Respuesta inválida. Por favor, ingrese 'sí', 's' o 'no', 'n'.")

    # Guardar los horarios de los Trainers en un archivo JSON
    with open("horariosTrainers.json", "w") as archivo:
        json.dump(horariosTrainer, archivo, indent=4)

    with open("horariosTrainers.json", "r") as archivo:
        LeerHorario = json.load(archivo)
        print(LeerHorario)
    RegresarCoordinacion.regresarMenuC()

