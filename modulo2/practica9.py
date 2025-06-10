# Extracto de Iniciales

# Solicitar el nombre completo del usuario
nombre_completo = input("Ingrese su nombre completo: ")

# Separar el nombre en palabras
palabras = nombre_completo.split()

# Extraer las iniciales y formatearlas con punto
iniciales = ". ".join([palabra[0].upper() for palabra in palabras]) + "."

# Mostrar las iniciales
print(f"Las iniciales son: {iniciales}")
