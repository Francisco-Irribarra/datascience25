usuarios = {
    "usuario1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
    },
    "usuario2": {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona",
    },
    "usuario3": {
        "nombre": "Luis",
        "edad": 35,
        "ciudad": "Valencia",
    },
}
 
for usuario, edad in usuarios.items():
    print(f"{usuario.edad}")
    promedio_edad = sum(edad) / len(usuario)
print(f"promedio de edad: {promedio_edad}")  
 
 usuarios = {
    "usuario1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
    },
    "usuario2": {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona",
    },
    "usuario3": {
        "nombre": "Luis",
        "edad": 35,
        "ciudad": "Valencia",
    },
}
 
edades = [datos["edad"] for datos in usuarios.values()]
promedio_edad = sum(edades) / len(edades)
print("Promedio de edad de los usuarios:", promedio_edad)

