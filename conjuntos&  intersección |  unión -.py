# =========================
# 🏋️‍♂️ SISTEMA GYM
# =========================

# Conjuntos de clases
basico = {1, 2}
premium = {1, 2, 3, 4, 5}
vip = {1, 2, 3, 4, 5, 6, 7}

# Clases exclusivas por membresía
def exclusivas_por_membresia():
    return {
        "BASICO": basico - premium - vip,   # Vacío
        "PREMIUM": premium - basico - vip,  # Vacío
        "VIP": vip - premium               # Solo VIP
    }

# Clases en al menos dos membresías
def repetidas_en_al_menos_dos():
    return (basico & premium) | (premium & vip) | (basico & vip)

# Clases disponibles para todos
def para_todos():
    return basico & premium & vip

# Mostrar clases por membresía
def mostrar_clases_por_membresia():
    membre = input("Ingrese la membresía (BASICO, PREMIUM, VIP): ").upper()

    if membre == "BASICO":
        print("Clases:", basico)
    elif membre == "PREMIUM":
        print("Clases:", premium)
    elif membre == "VIP":
        print("Clases:", vip)
    else:
        print("Membresía no válida.")

# Menú del gym
def menu_gym():
    while True:
        print("\n--- MENÚ GYM ---")
        print("1. Exclusivas de cada membresía")
        print("2. Clases en al menos dos membresías")
        print("3. Clases para todos")
        print("4. Mostrar clases por membresía")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(exclusivas_por_membresia())
        elif opcion == "2":
            print(repetidas_en_al_menos_dos())
        elif opcion == "3":
            print(para_todos())
        elif opcion == "4":
            mostrar_clases_por_membresia()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


# =========================
# 🏪 SISTEMA SUCURSALES
# =========================

sucursal_1 = {"Arroz", "Sal", "Mantequilla"}
sucursal_2 = {"Arroz", "Sal", "Frijol", "Aceite", "Azucar", "Papa"}
sucursal_3 = {"Arroz", "Sal", "Frijol", "Aceite", "Azucar", "Salchicha", "Cafe"}

# Productos en todas
def disponibles_en_todas():
    return sucursal_1 & sucursal_2 & sucursal_3

# Productos exclusivos por sucursal
def exclusivas_por_sucursal():
    return {
        "SUCURSAL 1": sucursal_1 - sucursal_2 - sucursal_3,
        "SUCURSAL 2": sucursal_2 - sucursal_1 - sucursal_3,
        "SUCURSAL 3": sucursal_3 - sucursal_1 - sucursal_2
    }

# Productos en al menos dos pero no en todas
def en_al_menos_dos_pero_no_todas():
    return ((sucursal_1 & sucursal_2) |
            (sucursal_2 & sucursal_3) |
            (sucursal_1 & sucursal_3)) - disponibles_en_todas()

# Buscar producto
def mostrar_sucursales_por_producto():
    producto = input("Ingrese el producto: ").capitalize()

    disponible_en = []

    if producto in sucursal_1:
        disponible_en.append("SUCURSAL 1")
    if producto in sucursal_2:
        disponible_en.append("SUCURSAL 2")
    if producto in sucursal_3:
        disponible_en.append("SUCURSAL 3")

    if disponible_en:
        print("Disponible en:", ", ".join(disponible_en))
    else:
        print("No disponible en ninguna sucursal.")

# Menú sucursales
def menu_sucursales():
    while True:
        print("\n--- MENÚ SUCURSALES ---")
        print("1. Productos en todas")
        print("2. Productos exclusivos")
        print("3. En al menos dos pero no en todas")
        print("4. Buscar producto")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(disponibles_en_todas())
        elif opcion == "2":
            print(exclusivas_por_sucursal())
        elif opcion == "3":
            print(en_al_menos_dos_pero_no_todas())
        elif opcion == "4":
            mostrar_sucursales_por_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


# =========================
# 🧭 MENÚ PRINCIPAL
# =========================

def menu_principal():
    while True:
        print("\n=== SISTEMA GENERAL ===")
        print("1. Gym")
        print("2. Sucursales")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gym()
        elif opcion == "2":
            menu_sucursales()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


# Ejecutar programa
menu_principal()
