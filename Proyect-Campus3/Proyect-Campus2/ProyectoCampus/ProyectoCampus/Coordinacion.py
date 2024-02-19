import ExamenIngreso
import Eliminar_Campers_Trainers
import RegresarMain
import CrearRutas
import AsignamientoCampers_Trainers
import NotasModulo
import Horarios

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

OpcionEscogida = ["           *Bienvenido al menu de Coordinacion*",
    "═════════════════════════════════════════════════════════",
    "A continuacion, se le presentan las siguientes opciones:",
    "",
    "1. Actualizar nota de ingreso de los campers",
    "",
    "2. Actualizar notas de los filtros",
    "",
    "3. Eliminar/Denegar Campers y Trainers",
    "",
    "4. Crear nuevas rutas",
    "",
    "5. Añadir horarios de clase",
    "",
    "6. Asignar Campers y Trainers",
    "",
    "7. Salir"
    
]

def TerminarMenuCoordinacion():
    print("Has decidido salir del menu 'Gestion de Campers'.")
    print("")
    print("Volviendo al menu principal...")
    #Añadir funcion time
    RegresarMain.RegresarAlMain()



def contraseña():
    
    contraseñaCoordinacion = "CampusLand-2024"
    
    intentosMaximos = 3
    intentos = 0
    
    while intentos < intentosMaximos:
        
        intentos += 1
        contrasena_ingresada = input("Ingrese la contraseña: ")
        
        if contrasena_ingresada == contraseñaCoordinacion:
            print("Contraseña correcta. Permitiendo ingreso al perfil 'coordinacion'.")
            break
        else:
            intentosRestantes = intentosMaximos - intentos
            if intentosRestantes > 0:
                print(f"Contraseña incorrecta. Le quedan {intentosRestantes} intentos.")
            else:
                print("Ha alcanzado el máximo número de intentos permitidos.")
                print("")
                print("Deteniendo todo el sistema CAMPUSLAND...")
                #Añadir funcion time
                exit()

def MenuCoordinacion():
    while True:
        try:
            contraseña()
            
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            Opc = int(input("Ingresa el identificador de la opcion deseada: "))
            
            print("")
            
            if Opc == 1:
                
                ExamenIngreso.NotasExamenIngreso()
                
            elif Opc == 2:
                
                NotasModulo.AñadirNotasModulo()
                
            elif Opc == 3:
                
                Eliminar_Campers_Trainers.Eliminacion_Campers_Trainers()

            elif Opc == 4:
                
                CrearRutas.CrearRutasNuevas()
                
            elif Opc == 5:
                
                Horarios.añadirHorarios()
                
            elif Opc == 6:
                
                AsignamientoCampers_Trainers.MenuAsignacion()
                
            elif Opc == 7:
                
                TerminarMenuCoordinacion()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")

def MenuCoordinacion2():
    while True:
        try:
            
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            Opc = int(input("Ingresa el identificador de la opcion deseada: "))
            
            print("")
            
            if Opc == 1:
                
                ExamenIngreso.NotasExamenIngreso()
                
            elif Opc == 2:
                
                NotasModulo.AñadirNotasModulo()
                
            elif Opc == 3:
                
                Eliminar_Campers_Trainers.Eliminacion_Campers_Trainers()
                
            elif Opc == 4:
                
                CrearRutas.CrearRutasNuevas()
                
            elif Opc == 5:
                
                Horarios.añadirHorarios()
                
            elif Opc == 6:
                
                AsignamientoCampers_Trainers.MenuAsignacion()
                
            elif Opc == 7:
                
                TerminarMenuCoordinacion()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")
