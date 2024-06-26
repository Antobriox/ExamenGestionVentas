from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'bpodpedbpytr3ztavoei-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'untt7ovn5opdws4y'
app.config['MYSQL_PASSWORD'] = 'bX0HCukffFM2nBx4T4h6'
app.config['MYSQL_DB'] = 'bpodpedbpytr3ztavoei'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def index():
    # Obtener la ruta de la carpeta templates
    template_folder = os.path.join(app.root_path, 'templates')

    # Obtener todos los archivos HTML en la carpeta templates
    html_files = [file for file in os.listdir(template_folder) if file.endswith('.html')]

    # Renderizar cada archivo HTML en la carpeta templates
    rendered_templates = []
    for html_file in html_files:
        with open(os.path.join(template_folder, html_file), 'r') as file:
            rendered_templates.append(file.read())

    return '<br>'.join(rendered_templates)

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Usuarios")
    usuarios = cur.fetchall()
    cur.close()
    return jsonify(usuarios)

# Ruta para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nombre = request.json['nombre']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Usuario creado exitosamente"})

# Ruta para obtener todos los proyectos
@app.route('/proyectos', methods=['GET'])
def get_proyectos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Proyectos")
    proyectos = cur.fetchall()
    cur.close()
    return jsonify(proyectos)

# Ruta para crear un nuevo proyecto
@app.route('/proyectos', methods=['POST'])
def crear_proyecto():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Proyectos (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Proyecto creado exitosamente"})

# Ruta para obtener todas las tareas
@app.route('/tareas', methods=['GET'])
def get_tareas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tareas")
    tareas = cur.fetchall()
    cur.close()
    return jsonify(tareas)

# Ruta para crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    fecha_limite = request.json['fecha_limite']
    id_proyecto = request.json['id_proyecto']
    id_usuario = request.json['id_usuario']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Tareas (titulo, descripcion, fecha_limite, id_proyecto, id_usuario) VALUES (%s, %s, %s, %s, %s)", (titulo, descripcion, fecha_limite, id_proyecto, id_usuario))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Tarea creada exitosamente"})

# Ruta para actualizar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    nombre = request.json['nombre']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Usuarios SET nombre=%s, email=%s WHERE id=%s", (nombre, email, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Usuario actualizado exitosamente"})

# Ruta para actualizar un proyecto
@app.route('/proyectos/<int:id>', methods=['PUT'])
def actualizar_proyecto(id):
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Proyectos SET nombre=%s, descripcion=%s WHERE id=%s", (nombre, descripcion, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Proyecto actualizado exitosamente"})

# Ruta para actualizar una tarea
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    fecha_limite = request.json['fecha_limite']
    id_proyecto = request.json['id_proyecto']
    id_usuario = request.json['id_usuario']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Tareas SET titulo=%s, descripcion=%s, fecha_limite=%s, id_proyecto=%s, id_usuario=%s WHERE id=%s", (titulo, descripcion, fecha_limite, id_proyecto, id_usuario, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Tarea actualizada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
