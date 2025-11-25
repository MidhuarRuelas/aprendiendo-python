# Métodos de listas

print("=== MODIFICANDO LISTAS ===\n")

# Lista inicial
tareas = ["estudiar", "cocinar", "ejercicio"]
print(f"Lista inicial: {tareas}")

# APPEND - Agregar al final
tareas.append("leer")
print(f"\nDespués de append('leer'): {tareas}")

# INSERT - Insertar en posición específica
tareas.insert(1, "comprar")  # Posición 1
print(f"Después de insert(1, 'comprar'): {tareas}")

# REMOVE - Eliminar por valor
tareas.remove("cocinar")
print(f"Después de remove('cocinar'): {tareas}")

# POP - Eliminar último elemento
eliminado = tareas.pop()
print(f"Después de pop(): {tareas}")
print(f"Elemento eliminado: {eliminado}")

# POP con índice - Eliminar en posición específica
eliminado = tareas.pop(0)
print(f"Después de pop(0): {tareas}")
print(f"Elemento eliminado: {eliminado}")

# SORT - Ordenar alfabéticamente
numeros = [50, 10, 30, 20, 40]
print(f"\nNúmeros desordenados: {numeros}")
numeros.sort()
print(f"Números ordenados: {numeros}")

# REVERSE - Invertir orden
numeros.reverse()
print(f"Números invertidos: {numeros}")