import json

# Función para asignar rutas a campistas aprobados
def AsignarCampers(Campers, RutasDefinidas):
    Campers["Estado"] = "Aprobado"
    for camper in Campers:
        if Campers["Estado"] == "Aprobado":
            for ruta in  RutasDefinidas:
                if len(RutasDefinidas["campers"]) < 33:
                    Campers["Ruta asignada"] = RutasDefinidas["Java"]
                    RutasDefinidas["Java"].append(camper)
                    break

# Función para asignar entrenadores a rutas de entrenamiento
def AsignarTrainers(Trainers, RutasDefinidas):
    for trainer in Trainers:
        for ruta in RutasDefinidas:
            "INVESTIGAR QUE SIGNIFICA"
            if RutasDefinidas["Java"] in Trainers["name"] and ruta not in RutasDefinidas["Ruta asignada"]:
                Trainers["Ruta asignada"].append(ruta)

# Función para matricular campistas aprobados en rutas de entrenamiento
def DatosRutaAsignada(camper, route, trainer, start_date, end_date, training_room):
    camper["route_assigned"] = route["name"]
    camper["start_date"] = start_date
    camper["end_date"] = end_date
    camper["trainer_assigned"] = trainer["name"]
    camper["training_room"] = training_room
    route["camper_list"].append(camper)

# Cargar datos desde archivos JSON
with open("Campers.json", "r") as f:
    campers_data = json.load(f)

with open("Trainers.json", "r") as f:
    trainers_data = json.load(f)

with open("Rutas.json", "r") as f:
    routes_data = json.load(f)

# Asignar rutas a campistas aprobados
AsignarCampers(campers_data, routes_data)

# Asignar entrenadores a rutas de entrenamiento
AsignarTrainers(trainers_data, routes_data)

# Matricular campistas aprobados en rutas de entrenamiento
DatosRutaAsignada(campers_data[0], routes_data[0], trainers_data[0], "2024-02-15", "2024-03-15", "Sputnik")
DatosRutaAsignada(campers_data[1], routes_data[1], trainers_data[1], "2024-02-15", "2024-03-15", "Apolo")
DatosRutaAsignada(campers_data[3], routes_data[2], trainers_data[2], "2024-02-15", "2024-03-15", "Artemis")

# Ejemplo de acceso a la información de un camper
print("Nombre:", campers_data[0]["name"])
print("Ruta asignada:", campers_data[0]["route_assigned"])
print("Entrenador asignado:", campers_data[0]["trainer_assigned"])
print("Fecha de inicio:", campers_data[0]["start_date"])
print("Fecha de finalización:", campers_data[0]["end_date"])
print("Sala de entrenamiento:", campers_data[0]["training_room"])
