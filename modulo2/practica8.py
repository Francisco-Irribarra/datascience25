# Generador de Contraseña Simple

# Solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Solicitar un número
numero = input("Ingrese un número: ")

# Símbolo fijo para la contraseña
simbolo = "!"

# Generar la contraseña
contraseña = nombre + numero + simbolo

# Mostrar la contraseña generada
print(f"Su contraseña generada es: {contraseña}")
