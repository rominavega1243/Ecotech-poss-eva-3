from persistencia.crear_bd import crear_tablas
from menus import menu_empleado
from menus import menu_proyecto
from menus import menu_departamento
from menus import menu_registro_tiempo
from semilla_bd import cargar_semillas
from menu_usuario import solicitar_login, menu_privado

def mostrar_menu_sistema():
    while True:
        print("\n=== SISTEMA ===")
        print("1. Empleados")
        print("2. Proyectos")
        print("3. Departamentos")
        print("4. Registros de Tiempo")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_empleado.ejecutar_menu()
        elif opcion == "2":
            menu_proyecto.ejecutar_menu()
        elif opcion == "3":
            menu_departamento.ejecutar_menu()
        elif opcion == "4":
            menu_registro_tiempo.ejecutar_menu()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def main():
    while True:
        usuario_actual = solicitar_login()
        if usuario_actual is None:
            if input("Enter para reintentar o 0 para salir: ") == "0":
                return
            continue
        opcion = menu_privado(usuario_actual)
        usuario_actual = None # Terminar el acceso de esta sesión.
        if opcion == "0":
            return
        print("Sesión cerrada. Ingrese nuevamente.")

crear_tablas() 
cargar_semillas()
main()