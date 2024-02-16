import Campers
import Trainers

def Eliminacion_Campers_Trainers():
    print("¿Que deseas eliminar?")
    print("")
    print("1. |--Camper--|")
    print("")
    print("2. |--Trainer--|")
    eliminacion = int(input("Ingresa el identificador de la opcion a la cual quieres acceder: "))
    if eliminacion == 1:
        Campers.EliminarCamper()
    elif eliminacion == 2:
        Trainers.EliminarTrainer()
    else:
        print("No has ingresado un identificador aceptado")


