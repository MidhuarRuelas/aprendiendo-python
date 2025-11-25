# Gestor de Tareas (TODO List)

print("=" * 40)
print("   📝 GESTOR DE TAREAS")
print("=" * 40)

# Lista de tareas (vacía al inicio)
tareas = []

while True:
    # Mostrar menú
    print("\n--- MENÚ ---")
    print("1. Ver todas las tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    
    opcion = input("\nElige una opción (1-5): ")
    
    # OPCIÓN 1: Ver tareas
    if opcion == "1":
        print("\n--- MIS TAREAS ---")
        if len(tareas) == 0:
            print("❌ No tienes tareas pendientes")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
    
    # OPCIÓN 2: Agregar tarea
    elif opcion == "2":
        nueva_tarea = input("\n¿Qué tarea quieres agregar? ")
        tareas.append(nueva_tarea)
        print(f"✅ Tarea '{nueva_tarea}' agregada")
    
    # OPCIÓN 3: Marcar como completada
    elif opcion == "3":
        if len(tareas) == 0:
            print("\n❌ No hay tareas para completar")
        else:
            print("\n--- TAREAS PENDIENTES ---")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            
            try:
                numero = int(input("\n¿Cuál completaste? (número): "))
                if 1 <= numero <= len(tareas):
                    tarea_completada = tareas[numero - 1]
                    print(f"✅ ¡Completaste: '{tarea_completada}'!")
                else:
                    print("❌ Número inválido")
            except:
                print("❌ Debes escribir un número")
    
    # OPCIÓN 4: Eliminar tarea
    elif opcion == "4":
        if len(tareas) == 0:
            print("\n❌ No hay tareas para eliminar")
        else:
            print("\n--- TAREAS ACTUALES ---")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            
            try:
                numero = int(input("\n¿Cuál quieres eliminar? (número): "))
                if 1 <= numero <= len(tareas):
                    tarea_eliminada = tareas.pop(numero - 1)
                    print(f"🗑️ Tarea '{tarea_eliminada}' eliminada")
                else:
                    print("❌ Número inválido")
            except:
                print("❌ Debes escribir un número")
    
    # OPCIÓN 5: Salir
    elif opcion == "5":
        print("\n👋 ¡Hasta luego! Sigue siendo productivo")
        break
    
    # Opción inválida
    else:
        print("\n❌ Opción inválida. Intenta de nuevo")