from persistencia.crear_bd import crear_tablas
from menus import menu_empleado
from menus import menu_proyecto
from menus import menu_departamento
from menus import menu_registro_tiempo

def main():
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

crear_tablas()
main()