import json
import Aprovados_Reprovados


def mostrarMenu():
    print("╔═════════════════════════════════════════╗")
    print("║           Módulo de Reportes            ║")
    print("╠═════════════════════════════════════════╣")
    print("║ 1. Listar campers inscritos             ║")
    print("║ 2. Listar campers aprobados             ║")
    print("║ 3. Listar entrenadores trabajando       ║")
    print("║ 4. Listar campers con bajo rendimiento  ║")
    print("║ 5. Listar campers y entrenadores en ruta║")
    print("║ 6. Mostrar campers perdidos y aprobados ║")
    print("║ 7. Salir                                ║")
    print("╚═════════════════════════════════════════╝")

def menuReportes():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            
            with open("Campers.json", "r") as archivo:
                CampersInscritos = json.load(archivo)
                print("Registros de los campers inscritos")
                print(CampersInscritos)
            pass
        elif opcion == "2":
            
            with open('CampersAprovados.json', 'r') as archivo:
                LeerNotas = json.load(archivo)
                print("Registros de los campers aprovados")
                print(LeerNotas)
            pass
        elif opcion == "3":
            
            with open("Trainers.json", "r") as archivo:
                TrainersTrabajando = json.load(archivo)
                print("Trainers Trabajando actualmente:")
                print(TrainersTrabajando)
            pass
        elif opcion == "4":
            with open('NotasExamenModulo.json', 'r') as archivo:
                RiesgoCamper = json.load(archivo)
                print(RiesgoCamper)
            pass
        elif opcion == "5":
            
            with open('Areas.json', 'r') as archivo:
                Campers_Trainers = json.load(archivo)
                print(Campers_Trainers)
            pass
        elif opcion == "6":
            
            Aprovados_Reprovados.CampersAprovados_Reprovadors()
            pass
        elif opcion == "7":
            print("Saliendo del módulo de reportes...")
            print("")
            print("Solicitud completada.")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")