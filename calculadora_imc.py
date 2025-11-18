# Calculadora de IMC (Índice de Masa Corporal)

# Preguntar el nombre
nombre = input("¿Cuál es tu nombre? ")

# Preguntar el peso (número entero)
peso = int(input("¿Cuál es tu peso en kg? "))

# Preguntar la altura (en centímetros para usar enteros)
altura_cm = int(input("¿Cuál es tu altura en centímetros? (ej: 175) "))

# Convertir altura a metros (de centímetros a metros)
altura_m = altura_cm / 100

# Calcular el IMC
imc = peso / (altura_m * altura_m)

# Interpretar el IMC
if imc < 18.5:
    diagnostico = "Bajo peso"
elif imc < 25:
    diagnostico = "Peso normal"
elif imc < 30:
    diagnostico = "Sobrepeso"
else:
    diagnostico = "Obesidad"

# Mostrar el resultado
print("\n--- RESULTADO ---")
print(f"Nombre: {nombre}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura_cm} cm ({altura_m} m)")
print(f"IMC = {peso} / ({altura_m} × {altura_m}) = {imc:.2f}")
print(f"Diagnóstico: {diagnostico}")