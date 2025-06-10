# # Parte 1: Recorrer una palabra e imprimir posición y letra

# palabra = "gato"
# indice = 0

# while indice < len(palabra):
#     print(f"Letra en posición {indice}: {palabra[indice]}")
#     indice += 1

# # Parte 2: Contar del 1 al 5 y validar si es par o impar

# numero = 1
# while numero <= 5:
#     if numero % 2 == 0:
#         print(f"El número {numero} es par")
#     else:
#         print(f"El número {numero} es impar")
#     numero += 1


# #Menu while
# opcion = ""
# while opcion != "4":
#     print("1. suma")
#     print("2. resta 2")
#     print("3. multiplicacion")
#     print("4. Salir")
#     opcion = input("Seleccione una opción: ")
    
#     if opcion == "1":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 + numero2
#         print(f"La suma de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "2":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 - numero2
#         print(f"La resta de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "3":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 * numero2
#         print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida, por favor intente de nuevo.")
 

# Función para pedir 4 números con validación
def ingresar_numeros():
    numeros = []
    for i in range(4):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")
    return numeros

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Calcular y mostrar la suma total de los números")
    print("2. Calcular y mostrar el promedio de los números")
    print("3. Mostrar el número mayor y menor")
    print("4. Salir")

# Programa principal
numeros = ingresar_numeros()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        suma = sum(numeros)
        print(f"La suma total de los números es: {suma}")
    elif opcion == "2":
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio}")
    elif opcion == "3":
        mayor = max(numeros)
        menor = min(numeros)
        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 4.")