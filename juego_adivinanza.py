# Juego de adivinanza
print("=== JUEGO DE ADIVINANZA ===")
print("Estoy pensando en un número del 1 al 10\n")

# Número secreto
numero_secreto = 7

# Pedir al usuario que adivine
intento = int(input("¿Qué número es? "))

# Evaluar el intento
if intento == numero_secreto:
    print("🎉 ¡CORRECTO! Adivinaste el número")
elif intento < numero_secreto:
    print("❌ Muy bajo. El número es más alto")
else:
    print("❌ Muy alto. El número es más bajo")

print(f"\nEl número era: {numero_secreto}")