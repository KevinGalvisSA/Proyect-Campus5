import Campers
import Trainers

def Eliminacion_Campers_Trainers():
    try:
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
    except Exception:
        print("¡¡¡Ha ocurrido un error!!!!")
        print("Intentaste ingresar una variable diferente a 'int'. Además no corresponde a ninguno de los identificadores permitidos.")


