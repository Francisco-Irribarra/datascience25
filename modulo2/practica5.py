# Solicitar al usuario el capital inicial
capital_inicial = float(input("Ingrese el capital inicial: "))

# Solicitar al usuario la tasa de interés (en porcentaje)
tasa_interes = float(input("Ingrese la tasa de interés (en porcentaje): "))

# Solicitar al usuario el número de años
numero_anios = int(input("Ingrese el número de años: "))

# Calcular el interés simple
interes_simple = (capital_inicial * tasa_interes * numero_anios) / 100

# Mostrar el resultado
print(f"El interés simple es: {interes_simple:.2f}")
