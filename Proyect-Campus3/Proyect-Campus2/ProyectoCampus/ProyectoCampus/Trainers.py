import json
import RegresarMain

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
    #Añadir funcion time
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
            
            print("")
            
            if opc == 1:
                
                RegistroTrainer()
                
            elif opc == 2:
                
                print("En Desarrollo")
                
            elif opc == 3:
                
                MostrarTrainers()
                
            elif opc == 4:
                
                TerminarMenuTrainer()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")
