# Cálculo de Longitud de Nombre

# Solicitar el nombre y apellido del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Combinar nombre y apellido en una sola cadena (sin espacios adicionales)
nombre_completo = nombre.strip() + " " + apellido.strip()

# Calcular la longitud total (incluye el espacio entre nombre y apellido)
longitud = len(nombre_completo)

# Mostrar el resultado
print(f"Su nombre completo es: {nombre_completo}")
print(f"La longitud total de la cadena es: {longitud} caracteres")
