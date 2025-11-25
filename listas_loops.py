# Loops con listas

print("=== LOOPS CON LISTAS ===\n")

# Lista de estudiantes
estudiantes = ["Ana", "Juan", "María", "Pedro", "Sofia"]

# Forma 1: Loop directo
print("--- Lista de estudiantes ---")
for estudiante in estudiantes:
    print(f"Hola {estudiante}")

# Forma 2: Con índice y enumerate
print("\n--- Con numeración ---")
for i, estudiante in enumerate(estudiantes, 1):  # Empieza desde 1
    print(f"{i}. {estudiante}")

# Sumar números de una lista
numeros = [10, 25, 30, 15, 20]
print(f"\n--- Números: {numeros} ---")

total = 0
for numero in numeros:
    total += numero
    print(f"Sumando {numero}... Total parcial: {total}")

print(f"\nSuma final: {total}")

# Filtrar elementos (solo números mayores a 20)
print("\n--- Números mayores a 20 ---")
for numero in numeros:
    if numero > 20:
        print(f"✅ {numero} es mayor a 20")
    else:
        print(f"❌ {numero} no es mayor a 20")