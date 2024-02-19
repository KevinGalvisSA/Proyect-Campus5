import json

def CampersAprovados_Reprovadors():
    with open('CampersReprovados.json', 'r') as archivo:
        LeerNotas = json.load(archivo)

    with open('CampersAprovados.json', 'r') as archivo:
        LeerNotas = json.load(archivo)

    with open('ExamenIngreso.json', 'w') as archivo:
        json.dump(LeerNotas, archivo, indent=4)
        print(LeerNotas)