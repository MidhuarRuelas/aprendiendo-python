# Mini calculadora con menú
print("=== CALCULADORA INTERACTIVA ===\n")

while True:
    # Mostrar menú
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    # Pedir opción
    opcion = input("\nElige una opción (1-5): ")
    
    # Opción de salir
    if opcion == "5":
        print("\n👋 ¡Hasta luego! Gracias por usar la calculadora")
        break
    
    # Validar opción
    if opcion not in ["1", "2", "3", "4"]:
        print("❌ Opción inválida. Intenta de nuevo")
        continue  # Vuelve al inicio del loop
    
    # Pedir números
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    
    # Realizar operación
    if opcion == "1":
        resultado = num1 + num2
        print(f"\n✅ {num1} + {num2} = {resultado}")
    elif opcion == "2":
        resultado = num1 - num2
        print(f"\n✅ {num1} - {num2} = {resultado}")
    elif opcion == "3":
        resultado = num1 * num2
        print(f"\n✅ {num1} × {num2} = {resultado}")
    elif opcion == "4":
        if num2 == 0:
            print("\n❌ ERROR: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print(f"\n✅ {num1} ÷ {num2} = {resultado:.2f}")