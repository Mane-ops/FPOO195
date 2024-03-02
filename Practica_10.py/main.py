from Persona import Usuario

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar usuario")
    print("2. Consultar información de usuario")
    print("3. Editar información de usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def agregar_usuario():
    print("\nRegistro")
    nombre = input("Registra tu nombre de usuario: ")
    correo = input("Registra tu correo: ")
    password = input("Registra tu contraseña: ")
    user = Usuario(nombre, correo, password)
    user.agregar()

def consultar_usuario():
    nombre_consulta = input("Ingrese el nombre del usuario a consultar: ")
    for user in Usuario.usuarios:
        if user.getNombre() == nombre_consulta:
            user.consultar()
            break
    else:
        print("Usuario no encontrado.")

def editar_usuario():
    nombre_editar = input("Ingrese el nombre del usuario a editar: ")
    for user in Usuario.usuarios:
        if user.getNombre() == nombre_editar:
            nombre_nuevo = input("Ingrese el nuevo nombre: ")
            correo_nuevo = input("Ingrese el nuevo correo: ")
            password_nuevo = input("Ingrese la nueva contraseña: ")
            user.editar(nombre_nuevo, correo_nuevo, password_nuevo)
            print("Usuario editado exitosamente.")
            break
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ")
    for user in Usuario.usuarios:
        if user.getNombre() == nombre_eliminar:
            user.eliminar()
            break
    else:
        print("Usuario no encontrado.")

if _name_ == "_main_":
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            agregar_usuario()
        elif opcion == 2:
            consultar_usuario()
        elif opcion == 3:
            editar_usuario()
        elif opcion == 4:
            eliminar_usuario()
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")