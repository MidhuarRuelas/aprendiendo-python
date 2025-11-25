# Listas básicas en Python

print("=== LISTAS BÁSICAS ===\n")

# Lista de frutas
frutas = ["manzana", "banana", "naranja", "uva", "fresa"]

print("Mi lista de frutas:")
print(frutas)

# Acceder a elementos individuales
print("\n--- Accediendo a elementos ---")
print(f"Primera fruta: {frutas[0]}")
print(f"Segunda fruta: {frutas[1]}")
print(f"Última fruta: {frutas[-1]}")  # -1 = último elemento
print(f"Penúltima fruta: {frutas[-2]}")  # -2 = penúltimo

# Cantidad de elementos
print(f"\nTotal de frutas: {len(frutas)}")

# Lista de números
numeros = [10, 25, 5, 40, 15, 30]

print("\n--- Operaciones con números ---")
print(f"Números: {numeros}")
print(f"Suma total: {sum(numeros)}")
print(f"Número mayor: {max(numeros)}")
print(f"Número menor: {min(numeros)}")