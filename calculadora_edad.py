# Calculadora de edad futura
print("=== CALCULADORA DE EDAD ===\n")

# Pedir datos (convirtiendo a números)
nombre = input("¿Cómo te llamas? ")
edad_actual = int(input("¿Cuántos años tienes? "))
años_futuros = int(input("¿Cuántos años quieres avanzar? "))

# Calcular
edad_futura = edad_actual + años_futuros

# Mostrar resultado
print("\n=== RESULTADO ===")
print(nombre + ", en", años_futuros, "años tendrás", edad_futura, "años")
print("¡Espero que sigas programando para entonces! 🚀")