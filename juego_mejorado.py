# Juego de adivinanza con múltiples intentos
import random

print("=== JUEGO DE ADIVINANZA MEJORADO ===")
print("Tienes intentos ilimitados hasta adivinar\n")

# Número secreto aleatorio
numero_secreto = random.randint(1, 10)

# Pedir nombre
nombre = input("¿Cómo te llamas? ")
print(f"\nHola {nombre}, ¡intenta adivinar el número del 1 al 10!\n")

# Contador de intentos
intentos = 0

# Loop mientras no adivine
while True:  # True = siempre verdadero (loop infinito)
    intentos += 1  # Suma 1 al contador
    
    intento = int(input(f"Intento #{intentos}: "))
    
    if intento == numero_secreto:
        print(f"\n🎉 ¡CORRECTO {nombre}!")
        print(f"Adivinaste en {intentos} intentos")
        break  # Rompe el loop (sale del while)
    elif intento < numero_secreto:
        print("❌ Muy bajo. Intenta de nuevo")
    else:
        print("❌ Muy alto. Intenta de nuevo")