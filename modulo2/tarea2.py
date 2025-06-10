# Panel de Control de Estudiantes

# Diccionario para almacenar estudiantes y sus calificaciones
estudiantes = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ver todos los estudiantes")
    print("2. Agregar un nuevo estudiante")
    print("3. Mostrar estudiantes aprobados y reprobados")
    print("4. Calcular el promedio general")
    print("5. Salir")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        if estudiantes:
            print("\nLista de estudiantes:")
            for nombre, nota in estudiantes.items():
                print(f"{nombre}: {nota}")
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "2":
        nombre = input("Nombre del estudiante: ").strip()
        if nombre in estudiantes:
            print("Ese estudiante ya existe.")
        else:
            try:
                nota = float(input("Nota del estudiante (0 a 100): "))
                if 0 <= nota <= 100:
                    estudiantes[nombre] = nota
                    print(f"Estudiante {nombre} agregado con nota {nota}.")
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Error: La nota debe ser un número válido.")
    
    elif opcion == "3":
        aprobados = {}
        reprobados = {}
        for nombre, nota in estudiantes.items():
            if nota >= 60:
                aprobados[nombre] = nota
            else:
                reprobados[nombre] = nota

        print("\nEstudiantes Aprobados:")
        for nombre, nota in aprobados.items():
            print(f"{nombre}: {nota}")

        print("\nEstudiantes Reprobados:")
        for nombre, nota in reprobados.items():
            print(f"{nombre}: {nota}")
    
    elif opcion == "4":
        if estudiantes:
            total = sum(estudiantes.values())
            promedio = total / len(estudiantes)
            print(f"Promedio general de calificaciones: {promedio:.2f}")
        else:
            print("No hay estudiantes registrados para calcular promedio.")
    
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta con un número del 1 al 5.")
        