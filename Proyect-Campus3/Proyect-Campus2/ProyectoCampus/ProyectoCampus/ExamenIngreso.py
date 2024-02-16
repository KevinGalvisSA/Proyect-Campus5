import json

def NotasExamenIngreso():
    # Cargar el archivo JSON
    with open('ExamenIngreso.json', 'r') as archivo:
        data = json.load(archivo)
    
    # Crear un nuevo diccionario con los datos del examen
    nombre = str(input("Ingrese el nombre del camper al cual se le asignara la nota: "))
    NotaTeorica = int(input("Ingrese el resultado de la nota del examen teorico: "))
    NotaPractica = int(input("Ingrese el resultado de la nota del examen practico: "))
    NotaSumadas = NotaPractica + NotaTeorica 
    NotaPromedio = NotaSumadas / 2
    
    if NotaPromedio < 60 :
        print("|-EXAMEN REPROVADO-|")
        print("El camper no puede ser aprovado.")
        exit()
    elif NotaPromedio >= 60 :
        print("|-EXAMEN APROVADO-|")
        print("El camper califica para ingresar a ||-CAMPUSLAND-||")
        NotaIngreso = NotaPromedio
        
    Resultados = {
        "Nombre": nombre,
        "Nota": NotaIngreso
    }
    
    # Agregar el resultado la lista de resultados en el archivo JSON
    data["Resultados"].append(Resultados)
    
    # Guardar los datos actualizados en el archivo JSON
    with open('ExamenIngreso.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)






