# Gestor de Números Pares e Impares

# Lista para almacenar los números
numeros = []

# Funciones auxiliares
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar un número a la lista")
    print("2. Ver la lista completa")
    print("3. Ver solo los números pares")
    print("4. Ver solo los números impares")
    print("5. Salir")

# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        try:
            numero = int(input("Ingresa un número entero: "))
            numeros.append(numero)
            print(f"Número {numero} agregado a la lista.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")
    
    elif opcion == "2":
        print("Lista completa:", numeros)
    
    elif opcion == "3":
        pares = [n for n in numeros if n % 2 == 0]
        print("Números pares:", pares)
    
    elif opcion == "4":
        impares = [n for n in numeros if n % 2 != 0]
        print("Números impares:", impares)
    
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor elige una opción del 1 al 5.")

