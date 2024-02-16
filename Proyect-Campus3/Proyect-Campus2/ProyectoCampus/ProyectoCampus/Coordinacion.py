import ExamenIngreso
import Eliminar_Campers_Trainers

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
    "1. Aprovar Campers y Trainers",
    "",
    "2. Actualizar nota de ingreso del camper",
    "",
    "3. Actualizar notas de los filtros.",
    "",
    "4. Eliminar/Denegar Campers y Trainers",
    "",
    "5. Crear nuevas rutas",
    "",
    "6. Añadir horarios de clase",
    "",
    "7. Asignar Campers y Trainers"
    "",
    "8. Salir"
    
]

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
                break

def MenuCoordinacion():
    while True:
        try:
            MuestraMenu(OpcionEscogida)
            
            print("")
            
            Opc = int(input("Ingresa el identificador de la opcion deseada: "))
            
            print("")
            
            if Opc == 1:
                
                "Modificar_Estado_RiesgoCamper()"
                
            elif Opc == 2:
                
                ExamenIngreso.NotasExamenIngreso()
                
            elif Opc == 3:
                
                "AñadirNotaFiltros()"
                
            elif Opc == 4:
                
                Eliminar_Campers_Trainers.Eliminacion_Campers_Trainers()
                
            elif Opc == 5:
                
                "CrearRutasNuevas()"
                
            elif Opc == 6:
                
                "AñadirHorarios()"
                
            elif Opc == 7:
                
                "AsignarCampers_Trainers()"
                
            elif Opc == 8:
                
                "TerminarMenuCoordinacion()"
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")


