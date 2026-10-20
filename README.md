# Ecotech-eva-3 #  # Titulo del repositorio #

crear_bd.py
semilla_bd.py

ia lo que me ayudo para que funcione el archivo semilla_bd.py

Puntos Clave y Correcciones Realizadas (con Soporte de IA)


Paso a Paso de las Correcciones Realizadas en semilla_bd.py1. 

1. Corrección de nombres de atributos en objetos (AttributeError)
Problema: El código intentaba acceder a depto_asignado.id, pero la clase Departamento no tenía una propiedad llamada id.

Solución: Se corrigió el nombre de la propiedad a depto_asignado.idDepartamento para alinearlo con el modelo de dominio.



2. Ajuste de parámetros en el constructor de Empleado (TypeError)
Problema: Al instanciar la clase Empleado, se estaban pasando 8 argumentos (incluyendo un None inicial y el ID de departamento), superando el límite aceptado por el constructor (__init__).

Solución: Se revisó la clase Empleado en la capa de dominio y se ajustó la llamada para enviar únicamente los 5 argumentos requeridos en su orden correspondiente: Empleado(nombre, correo, telefono, fecha, salario).


3. Eliminación de variables no utilizadas (Linter / SonarQube)
Problema: Aparecía la advertencia Remove the unused local variable "depto_asignado" porque la variable del departamento se calculaba pero ya no se usaba al instanciar al empleado.

Solución: Se eliminó la variable redundante para mantener el código limpio y sin advertencias de calidad.


4. Solución a errores de restricción NOT NULL en SQLite (IntegrityError)Problema: SQLite lanzaba errores de restricción NOT NULL constraint failed en empleado.nombre y proyecto.nombre.   

Solución: Se identificó que al pasar None al inicio del constructor, los argumentos se desplazaban una posición a la derecha, haciendo que la columna nombre recibiera None. Se removió el valor nulo inicial tanto en Empleado como en Proyecto(nombre, desc, fecha), logrando que los datos se insertaran correctamente en sus columnas.


5. Corrección en la instanciación de RegistroTiempo
Problema: Ocurría un TypeError al intentar pasar 6 argumentos a RegistroTiempo (incluyendo la descripción).

Solución: Se ajustó la llamada para enviar los 5 parámetros requeridos por la clase: RegistroTiempo(fecha, horas, tareas, emp_id, proy_id).


6. Eliminación de bucle infinito (Recursión no deseada)
Problema: El script quedaba ejecutándose indefinidamente después de completar los registros.

Solución: Se detectó que la función cargar_semillas() se estaba llamando a sí misma al final del archivo. Se eliminó la llamada interna redundante para que main.py la invoque una sola vez, guarde los cambios con conexion.commit(), cierre la conexión de forma segura y finalice la ejecución limpiamente.
