import mysql.connector

# Detalles de conexión a la base de datos en la nube
host = 'bpodpedbpytr3ztavoei-mysql.services.clever-cloud.com'
database = 'bpodpedbpytr3ztavoei'
user = 'untt7ovn5opdws4y'
password = 'bX0HCukffFM2nBx4T4h6'
port = 3306

# Crear una conexión a la base de datos
connection = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Cursor para ejecutar consultas SQL
cursor = connection.cursor()

# Definir las consultas SQL para crear las tablas
create_usuarios_table = """
CREATE TABLE Usuarios (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(100),
 email VARCHAR(100)
)
"""

create_proyectos_table = """
CREATE TABLE Proyectos (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(100),
 descripcion TEXT
)
"""

create_tareas_table = """
CREATE TABLE Tareas (
 id INT AUTO_INCREMENT PRIMARY KEY,
 titulo VARCHAR(100),
 descripcion TEXT,
 fecha_limite DATE,
 id_proyecto INT,
 id_usuario INT,
 FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id),
 FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
)
"""

# Ejecutar las consultas SQL para crear las tablas
cursor.execute(create_usuarios_table)
cursor.execute(create_proyectos_table)
cursor.execute(create_tareas_table)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()

print("Tablas creadas exitosamente en la base de datos.")
