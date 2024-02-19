import json
import RegresarMain
import time

Campers = {}

def registrarCamper():
    global Campers
    global documento
    documento = input("Ingrese el documento del participante: ")
    nombre = input("Ingrese el nombre del participante: ")
    edad = input("Ingrese la edad del participante: ")
    TelMov = input("Ingrese el número móvil del camper: ")
    TelFijo = input("Ingrese el número fijo del camper: ")
    estado = "Inscrito"
    
    Campers[documento] = {'nombre': nombre, 'edad': edad, 'telefono movil': TelMov, 'telefono fijo': TelFijo, 'estado': estado}
    
    with open("Campers.json", "w") as MuestraCampers:
        json.dump(Campers, MuestraCampers, indent=4)


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

OpcionEscogida = ["           *Bienvenido al menu de Campers*",
    "═════════════════════════════════════════════════════════",
    "A continuacion, se le presentan las siguientes opciones:",
    "",
    "1. Registrar Camper",
    "",
    "2. Mostrar Campers registrados",
    "",
    "3. Salir"
    
]

def MostrarCampers():
    global Campers
    with open("Campers.json", "r") as archivo:
            datosCampers = json.load(archivo)
            print("Aqui te presentamos los registros de los campers")
            print(datosCampers)

def TerminarMenuCamper():
    print("Has decidido salir del menu 'Gestion de Campers'.")
    print("")
    print("Volviendo al menu principal...")
    time.sleep(3)
    RegresarMain.RegresarAlMain()


def MenuCamper():
    while True:
        try:
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            Option = int(input("Ingresa el identificador de la opcion deseada: "))
            time.sleep(3)
            print("")
            
            if Option == 1:
                time.sleep(1)
                registrarCamper()
                time.sleep(1)
            elif Option == 2:
                time.sleep(1)
                MostrarCampers()
                time.sleep(1)
            elif Option == 3:
                time.sleep(1)
                TerminarMenuCamper()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")

