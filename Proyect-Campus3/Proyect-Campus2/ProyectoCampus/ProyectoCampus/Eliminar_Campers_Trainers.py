import json

def EliminarCamper():
    with open("Campers.json", "r") as archivo:
            datosCampers = json.load(archivo)
    documento = input("Ingrese el documento del camper a eliminar: ")
    copiaDatosCampers = datosCampers.copy()
    Listo = ((clave, valor) for clave, valor in copiaDatosCampers.items())
    for clave, valor in Listo:
        if clave == documento:
            del datosCampers[documento]
            #Añadir funcion time
            print("Camper eliminado con exito")
        else:
            print("No has ingresado el documento correcto")
    with open('Campers.json', 'w') as file:
        json.dump(datosCampers, file, indent=4)
    exit()


def EliminarTrainer():
    with open("Trainers.json", "r") as archivo:
            datosTrainers = json.load(archivo)
    documento = input("Ingrese el documento del camper a eliminar: ")
    Lista = [(clave, valor) for clave, valor in datosTrainers.items()]
    for clave, valor in Lista:
        if clave == documento:
            print("Entendido, procediendo a eliminar el registro del Trainer...")
            del datosTrainers[documento]
            #Añadir funcion time
            print("Trainer eliminado con exito")
    else:
        print("No has ingresado el documento correcto")
    with open('Trainers.json', 'w') as file:
        json.dump(datosTrainers, file, indent=4)
    exit()

def Eliminacion_Campers_Trainers():
    while True:
        try:
            print("¿Que deseas eliminar?")
            print("")
            print("1. |--Camper--|")
            print("")
            print("2. |--Trainer--|")
            print("")
            delete = int(input("Ingresa el identificador de la opcion a la cual quieres acceder: "))
            if delete == 1:
                EliminarCamper()
            elif delete == 2:
                EliminarTrainer()
            else:
                print("No has ingresado un identificador aceptado")
        except ValueError:
            print("¡¡¡Ha ocurrido un error!!!!")
            print("Intentaste ingresar una variable diferente a 'int'. Además no corresponde a ninguno de los identificadores permitidos.")

