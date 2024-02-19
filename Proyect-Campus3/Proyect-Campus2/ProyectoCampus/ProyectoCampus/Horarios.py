import json
import RegresarCoordinacion

def cargar_trainers():
    with open('Trainers.json', 'r') as archivo:
        trainers = json.load(archivo)
    return trainers

def crearHorariosTrainers(trainers):
    horariosTrainer = {}
    for trainer_id, trainer_data in trainers.items():
        rutas = trainer_data.get("rutas", [])
        horariosTrainer[trainer_id] = {ruta: False for ruta in rutas}
    return horariosTrainer

def puede_dirigir_trainer(trainer_id, ruta, horariosTrainer):
    return horariosTrainer.get(trainer_id, {}).get(ruta, False)

def añadirHorarios():
# Cargar los datos de los Trainers desde el archivo JSON
    trainers = cargar_trainers()

    # Crear los horarios de los Trainers
    horariosTrainer = crearHorariosTrainers(trainers)

    # Solicitar al usuario que ingrese el ID del Trainer y la ruta que desea verificar
    trainer_id = input("Ingrese el ID del Trainer: ")
    ruta = input("Ingrese la ruta que desea verificar: ")

    # Verificar si el Trainer puede dirigir la ruta especificada
    if trainer_id not in trainers:
        print("El documento ingresado no está registrado.")
    else:
        if puede_dirigir_trainer(trainer_id, ruta, horariosTrainer):
            print(f"El Trainer {trainer_id} puede dirigir la ruta {ruta}")
        else:
            print(f"El Trainer {trainer_id} no puede dirigir la ruta {ruta}")

        # Solicitar al usuario si desea permitir que el Trainer dirija la ruta especificada
        decision = input("¿Desea permitir que el Trainer dirija esta ruta? (sí/no): ").lower()
        if decision == "s" or decision == "si":
            horariosTrainer[trainer_id][ruta] = True
            print(f"Se ha permitido que el Trainer {trainer_id} dirija la ruta {ruta}")
        elif decision == "n" or decision == "no":
            print(f"No se permite que el Trainer {trainer_id} dirija la ruta {ruta}")
        else:
            print("Respuesta inválida. Por favor, ingrese 'sí', 's' o 'no', 'n'.")

    # Guardar los horarios de los Trainers en un archivo JSON
    with open("horariosTrainers.json", "w") as archivo:
        json.dump(horariosTrainer, archivo, indent=4)
    RegresarCoordinacion.regresarMenuC()