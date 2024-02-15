import json
import Main

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
    
    Campers[documento] = {'nombre': nombre, 'edad': edad, 'documento': documento, 'telefono movil': TelMov, 'telefono fijo': TelFijo, 'Estado': estado, 'Riesgo': False}
    
    with open("Campers.json", "w") as MuestraCampers:
        
        json.dump(Campers, MuestraCampers, indent=4)
        
    with open("Campers.json", "r") as archivo:
        datosCampers = json.load(archivo)
        print("Aqui te presentamos los registros de los campers")
        print(datosCampers)


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
    "2. Eliminar Camper",
    "",
    "3. Mostrar Campers registrados",
    "",
    "4. Salir"
    
]

def EliminarCamper():
    global Campers
    doc = input("Ingrese el documento del camper a eliminar: ")
    if doc == documento:
        print("Entendido, procediendo a eliminar el registro del camper...")
        if documento in Campers:
            del Campers[documento]
        #Añadir funcion time
        print("Camper eliminado con exito")
    else:
        print("No has ingresado el documento correcto")

def MostrarCampers():
    global Campers
    for Camper in Campers:
        print("A continuacion, se le presentan los datos de los campers registrados.")
        print("")
        print(Campers)

def TerminarMenuCamper():
    print("Has decidido salir del menu 'Gestion de Campers'.")
    print("")
    print("Volviendo al menu principal...")
    #Añadir funcion time
    Main.MenuPrincipal()


def MenuCamper():
    while True:
        try:
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            Option = int(input("Ingresa el identificador de la opcion deseada: "))
            
            print("")
            
            if Option == 1:
                
                registrarCamper()
                
            elif Option == 2:
                
                EliminarCamper()
                
            elif Option == 3:
                
                MostrarCampers()
                
            elif Option == 4:
                
                TerminarMenuCamper()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")
