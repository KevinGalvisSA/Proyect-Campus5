import json
import RegresarMain
import time

Trainers = {}

def RegistroTrainer():
    global Trainers
    global documento
    documento = input("Ingrese el documento del Trainer: ")
    nombre = input("Ingrese el nombre del Trainer: ")
    edad = input("Ingrese la edad del Trainer: ")
    TelMov = input("Ingrese el número móvil del Trainer: ")
    
    Trainers[documento]={"Nombre": nombre, "Edad": edad, "Telefono Movil": TelMov}
    
    with open("Trainers.json", "w") as MuestraTrainers:
        json.dump(Trainers, MuestraTrainers, indent=4)

def MostrarTrainers():
    global Trainers
    with open("Trainers.json", "r") as archivo:
            datosTrainers = json.load(archivo)
            print("Aqui te presentamos los registros de los campers")
            print(datosTrainers)


def TerminarMenuTrainer():
    print("Has decidido salir del menu 'Gestion de Trainers'.")
    print("")
    print("Volviendo al menu principal...")
    time.sleep(3)
    RegresarMain.RegresarAlMain()


def MuestraMenu(Opciones):
    #Calcular longitud maxima de las opciones
    LongitudMaxima = max(len(Opcion) for Opcion in Opciones)
    
    #Longitud del borde
    LongitudBorde = LongitudMaxima + 1
    
    print("╔" + "═" * LongitudBorde  + "╗")
    
    #Imprimir opciones
    for Opcion in Opciones:
        espaciosFaltantes = LongitudMaxima - len(Opcion)
        print("║ " + Opcion + " " * espaciosFaltantes + "║")
    
    print("╚" + "═" * LongitudBorde + "╝")

OpcionEscogida = ["           *Bienvenido al Menu del Trainer*",
    "═════════════════════════════════════════════════════════",
    "A continuacion, se le presentan las siguientes opciones:",
    "",
    "1. Informacion del Trainer",
    "",
    "2. Checking Rutas",
    "",
    "3. Mostrar Trainers",
    "",
    "4. Salir"
]


def MenuTrainer():
    while True:
        try:
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            opc = int(input("Ingresa el identificador de la opcion deseada: "))
            time.sleep(3)
            print("")
            
            if opc == 1:
                time.sleep(1)
                RegistroTrainer()
                
            elif opc == 2:
                
                with open('Areas.json', 'r') as archivo_areas:
                    Areas = json.load(archivo_areas)
                    print("Aqui te presentamos las rutas defidas disponibles")
                    time.sleep(1)
                    print(Areas)
                print("")
                print("Ademas. Te presentamos las rutas que estan en fase de creacion")
                print("")
                with open("RutasNuevas.json", "r") as archivo:
                    datos = json.load(archivo)
                    time.sleep(1)
                    print(datos)
                
            elif opc == 3:
                time.sleep(1)
                MostrarTrainers()
                
            elif opc == 4:
                time.sleep(1)
                TerminarMenuTrainer()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")
