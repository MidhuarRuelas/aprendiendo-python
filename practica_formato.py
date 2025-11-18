# Experimentando con f-strings y formato

nombre = "Midhuar"
edad = 40
altura = 1.78
peso = 94
saldo_banco = 1234567.89
porcentaje_avance = 0.75

print("=== EJEMPLOS DE F-STRINGS ===\n")

# Básico
print(f"1. Hola {nombre}")

# Con operaciones
print(f"2. En 5 años: {edad + 5} años")

# Decimales
print(f"3. Altura: {altura:.1f} metros")
print(f"4. Altura: {altura:.3f} metros")

# Sin decimales
print(f"5. Peso redondeado: {peso:.0f} kg")

# Números grandes
print(f"6. Saldo: ${saldo_banco:,.2f}")

# Porcentajes
print(f"7. Avance del curso: {porcentaje_avance:.0%}")
print(f"8. Avance del curso: {porcentaje_avance:.2%}")

# Alineación
print("\n=== ALINEACIÓN ===")
print(f"Izquierda  : |{nombre:<15}|")
print(f"Derecha    : |{nombre:>15}|")
print(f"Centro     : |{nombre:^15}|")