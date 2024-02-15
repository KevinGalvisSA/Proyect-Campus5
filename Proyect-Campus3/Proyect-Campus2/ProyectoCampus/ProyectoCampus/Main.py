import Main
import Trainers
import Campers

def MenuOpciones(Opciones):
    #Calcular longitud maxima de las opciones
    LongitudMaxima = max(len(Opcion) for Opcion in Opciones)
    
    #Longitud del borde
    LongitudBorde = LongitudMaxima + 2
    
    print("╔" + "═" * LongitudBorde  + "╗")
    
    #Imprimir opciones
    for Opcion in Opciones:
        espaciosFaltantes = LongitudMaxima - len(Opcion)
        print("║ " + Opcion + " " * espaciosFaltantes + " ║")
    
    print("╚" + "═" * LongitudBorde + "╝")


OpcionEscogida = ["                  *Bienvenido al Menu Principal*",
    "═════════════════════════════════════════════════════════════════════",
    "A continuacion, se le presentan las siguientes opciones:",
    "",
    "1. Acceder al menu *Campers*(|Registro-Eliminacion-Muestra|)",
    "",
    "2. Acceder al menu *Trainers*(|Registro-MuestraRutas-Asignacion|)",
    "",
    "3. Acceder al menu *Coordinacion*(|EstadoCamper-AsignacionTrainer|)",
    "",
    "5. Salir"
]

def TerminarMenuPrincipal():
    print("Has decidido salir del menu 'Principal'")
    print("")
    print("Volviendo al menu principal...")
    #Añadir funcion time
    exit()

def MenuPrincipal():
    global opc
    while (True):
        
        MenuOpciones(OpcionEscogida)
        
        print("")
        
        opc = int(input("Ingresa el identificador de la opción deseada: "))
        
        Main.MenuPrincipal2()

def MenuPrincipal2():
    global opc
    while (True):
        try:
            if opc  == 1:
                
                Campers.MenuCamper()
                
            elif opc  == 2:
                
                Trainers.MenuTrainer()
                
            elif opc  == 3:
                
                "Coordinador.MenuCoordinador"
                
            elif opc  == 4:
                
                TerminarMenuPrincipal()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")

MenuPrincipal()

