import mysql.connector

# Detalles de conexión a la base de datos en la nube
host = 'bpodpedbpytr3ztavoei-mysql.services.clever-cloud.com'
database = 'bpodpedbpytr3ztavoei'
user = 'untt7ovn5opdws4y'
password = 'bX0HCukffFM2nBx4T4h6'
port = 3306

# Datos para llenar las tablas
usuarios_data = [
    ("Juan", "juan@example.com"),
    ("María", "maria@example.com"),
    ("Pedro", "pedro@example.com")
]

proyectos_data = [
    ("Proyecto 1", "Descripción del Proyecto 1"),
    ("Proyecto 2", "Descripción del Proyecto 2"),
    ("Proyecto 3", "Descripción del Proyecto 3")
]

tareas_data = [
    ("Tarea 1", "Descripción de la Tarea 1", "2024-06-10", 1, 1),
    ("Tarea 2", "Descripción de la Tarea 2", "2024-06-15", 2, 2),
    ("Tarea 3", "Descripción de la Tarea 3", "2024-06-20", 3, 3)
]

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

# Insertar datos en la tabla Usuarios
insert_usuarios_query = "INSERT INTO Usuarios (nombre, email) VALUES (%s, %s)"
cursor.executemany(insert_usuarios_query, usuarios_data)

# Insertar datos en la tabla Proyectos
insert_proyectos_query = "INSERT INTO Proyectos (nombre, descripcion) VALUES (%s, %s)"
cursor.executemany(insert_proyectos_query, proyectos_data)

# Insertar datos en la tabla Tareas
insert_tareas_query = "INSERT INTO Tareas (titulo, descripcion, fecha_limite, id_proyecto, id_usuario) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_tareas_query, tareas_data)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()

print("Datos insertados exitosamente en las tablas.")
