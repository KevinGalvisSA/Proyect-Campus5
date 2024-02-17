import json
import Coordinacion


def NotasExamenIngreso():
    with open("Campers.json", "r") as Archivo:
        dato = json.load(Archivo)
    
    # Cargar el archivo JSON
    with open('ExamenIngreso.json', 'r') as archivo:
        data = json.load(archivo)
    
    # Crear un nuevo diccionario con los datos del examen
    nombre = str(input("Ingrese el nombre del camper al cual se le asignara la nota: "))
    
    for i in dato:
        if i["1095304280"]["nombre"] == nombre:
            print(f"Has decidio modificar las notas del camper -> {nombre}.")
            NotaTeorica = int(input("Ingrese el resultado de la nota del examen teorico: "))
            NotaPractica = int(input("Ingrese el resultado de la nota del examen practico: "))
            NotaSumadas = NotaPractica + NotaTeorica 
            NotaPromedio = NotaSumadas / 2
            
            if NotaPromedio < 60 :
                
                print("|-EXAMEN REPROVADO-|")
                print("El camper no puede ser aprovado.")
                for e in dato:
                    if e["1095304280"]["Estado"]=="Inscrito":
                        e["1095304280"]["Estado"]=="Aprovado"
                        NuevoEstado = e["1095304280"]["Estado"]
                        print(f"El nuevo estado del camper es: {NuevoEstado}.")
                        Coordinacion.MenuCoordinacion()
                
            elif NotaPromedio >= 60 :
                
                print("|-EXAMEN APROVADO-|")
                print("El camper califica para ingresar a ||-CAMPUSLAND-||")
                
                for o in dato:
                    if o["1095304280"]["Estado"]=="Inscrito":
                        o["1095304280"]["Estado"]=="Aprovado"
                        NuevoEstado = o["1095304280"]["Estado"]
                        print(f"El nuevo estado del camper es: {NuevoEstado}.")
                
                
                
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
            
            with open('ExamenIngreso.json', 'r') as archivo:
                LeerNotas = json.load(archivo)
            print("Ahora te presentamos las notas de los campers aceptados.")
            print(LeerNotas)
        
        
        elif i["1095304280"]["nombre"] != nombre:
            print(f"El camper que has seleccionado -> {nombre}. NO se encuentra registrado.")
            Coordinacion.MenuCoordinacion()


NotasExamenIngreso()




