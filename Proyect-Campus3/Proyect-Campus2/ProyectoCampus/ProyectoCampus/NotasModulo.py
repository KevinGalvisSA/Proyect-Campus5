import json
import RegresarCoordinacion
def cargar_camper_ids():
    with open('Campers.json', 'r') as archivo:
        Campers = json.load(archivo)
        CamperDocumento = list(Campers.keys())
        print(CamperDocumento)
    return CamperDocumento

def calcular_nota_final(pruebaTeoria, pruebaPractica, quizes, trabajos):
    # Calcular la nota final con los pesos dados
    nota_teoria = pruebaTeoria * 0.3
    nota_practica = pruebaPractica * 0.6
    nota_quizes = quizes * 0.05
    nota_trabajos = trabajos * 0.05

    # Calcular la nota final
    notaFinal = nota_teoria + nota_practica + nota_quizes + nota_trabajos
    notaDefinitiva = notaFinal
    return notaDefinitiva

def evaluar_modulo(documento, pruebaTeoria, pruebaPractica, quizes, trabajos):
    # Calcular la nota final
    notaDefinitiva = calcular_nota_final(pruebaTeoria, pruebaPractica, quizes, trabajos)

    # Determinar si el camper aprobó el módulo
    aprobado = notaDefinitiva >= 60
    if aprobado == True :
        riesgo = False
    else:
        riesgo = True

    # Crear un diccionario con los resultados

    resultados = {
        "documento": documento,
        "pruebaTeoria": pruebaTeoria,
        "pruebaPractica": pruebaPractica,
        "quizes": quizes,
        "trabajos": trabajos,
        "notaFinal": notaDefinitiva,
        "aprobado": aprobado,
        "riesgo": riesgo
    }

    return resultados

def guardar_resultados(resultados, NotasModulo):
    # Guardar los resultados en un archivo JSON
    with open(NotasModulo, 'w') as archivo:
        json.dump(resultados, archivo, indent=4)


def AñadirNotasModulo():
    # Obtener los IDs de los campers registrados
    CamperDocumento = cargar_camper_ids()

    # Solicitar al usuario que ingrese el ID del camper
    documento = input("Ingrese el documento del camper: ")

    # Verificar si el ID del camper ingresado está registrado
    if documento not in CamperDocumento:
        print("El documento ingresado no está registrado.")
    else:
        # Solicitar al usuario que ingrese los valores de las notas/pruebas
        pruebaTeoria = float(input("Ingrese la nota de la prueba teórica: "))
        pruebaPractica = float(input("Ingrese la nota de la prueba práctica: "))
        quizes = float(input("Ingrese la nota de los quizes: "))
        trabajos = float(input("Ingrese la nota de los trabajos: "))

        # Evaluar el módulo y obtener los resultados
        resultados = evaluar_modulo(documento, pruebaTeoria, pruebaPractica, quizes, trabajos)
        print("Resultados:", resultados)

        # Guardar los resultados en un archivo JSON
        NotasModulo = "NotasExamenModulo.json"
        guardar_resultados(resultados, NotasModulo)
        print(f"Resultados guardados con exito: \n'{NotasModulo}'")
    RegresarCoordinacion.regresarMenuC()