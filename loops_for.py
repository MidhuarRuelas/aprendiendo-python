# Ejemplos de FOR loops

print("=== EJEMPLO 1: Contar del 1 al 5 ===")
for i in range(1, 6):  # range(inicio, fin) - el fin NO se incluye
    print(f"Número: {i}")

print("\n=== EJEMPLO 2: Tabla de multiplicar ===")
numero = int(input("¿Tabla de multiplicar de qué número? "))
for i in range(1, 11):  # Del 1 al 10
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")

print("\n=== EJEMPLO 3: Cuenta regresiva ===")
for i in range(10, 0, -1):  # De 10 a 1, de atrás para adelante
    print(i)
print("🚀 ¡DESPEGUE!")