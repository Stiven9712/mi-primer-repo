estudiante = {
    "est1" : {"nombre":"Estiven","edad":"27 Años","programa":"ing. sofware"},
    "est2" : {"nombre":"pedro","edad":"25 Años","programa":"ing. Ambiental"}
}
estudiante ["est3"] = {"nombre":"Juan","edad":"25 Años","programa":"Derecho"}
estudiante ["est1"]["edad"]=28
estudiante ["est1"]["edad"]=21
estudiante ["est1"]["nombre"]="jose"
estudiante ["est3"]["programa"] = "administracion"
for clave,datos in estudiante.items():
    print(f"{clave}:nombre = {datos['nombre']}, edad = {datos['edad']}, programa = {datos['programa']}")
print("edad del estudiante 1", estudiante ["est1"]["programa"])