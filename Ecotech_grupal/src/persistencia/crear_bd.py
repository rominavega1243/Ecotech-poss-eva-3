from persistencia.conexion import abrir_conexion, obtener_motor

def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()

    # 1. Tabla empleado
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS empleado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            telefono TEXT,
            fecha_inicio_contrato TEXT,
            salario INTEGER
        );
        '''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS empleado (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(150) NOT NULL UNIQUE,
            telefono VARCHAR(20),
            fecha_inicio_contrato DATE,
            salario DECIMAL(10, 2)
        );
        '''
    cursor.execute(sql)

    # 2. Tabla departamento (Se eliminó la coma sobrante)
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS departamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            gerente TEXT
        );
        '''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS departamento (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            gerente VARCHAR(100)
        );
        '''
    cursor.execute(sql)

    # 3. Tabla proyecto (Se eliminó fecha_inicio duplicada)
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS proyecto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            fecha_inicio TEXT
        );
        '''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS proyecto (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(100) NOT NULL,
            descripcion VARCHAR(160),
            fecha_inicio DATE
        );
        '''
    cursor.execute(sql)

    # 4. Tabla registro_tiempo (Se corrigió sintaxis anidada y atributos según dominio)
    if obtener_motor() == "sqlite":
        sql = '''
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            cantidad_horas REAL,
            tareas_realizadas TEXT,
            descripcion TEXT
        );
        '''
    else:
        sql = '''
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id INT PRIMARY KEY AUTO_INCREMENT,
            fecha DATE,
            cantidad_horas DECIMAL(4, 2),
            tareas_realizadas VARCHAR(255),
            descripcion TEXT
        );
        '''
    cursor.execute(sql)

    conexion.commit()
    conexion.close()