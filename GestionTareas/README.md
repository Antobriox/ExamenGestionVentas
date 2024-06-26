# GestionTareas
Caso 1 hecho en la materia Calidad de Software

# Sistema de Gestión de Tareas

Este proyecto consiste en un Sistema de Gestión de Tareas desarrollado en Python utilizando el framework Flask para el backend y MySQL como base de datos en la nube. El sistema permite crear, ver, editar y eliminar usuarios, proyectos y tareas de manera interactiva a través de una interfaz de usuario web.

## Descargar el Proyecto

Para descargar y ejecutar este proyecto, sigue los siguientes pasos:

1. **Clonar el Repositorio**: 
   Clona este repositorio en tu máquina local utilizando el siguiente comando:
    git clone https://github.com/Karephilaky/GestionTareas.git


2. **Instalar Dependencias**:
Asegúrate de tener Python y pip instalados en tu sistema. Luego, instala las dependencias del proyecto ejecutando el siguiente comando:
  pip install -r requirements.txt


## Conexión a la Base de Datos en la Nube

Este proyecto utiliza una base de datos MySQL alojada en la nube para almacenar los datos de usuarios, proyectos y tareas. Sigue estos pasos para conectarte a la base de datos:

1. **Credenciales de la Base de Datos**:
Utiliza las siguientes credenciales para conectarte a la base de datos:
- **Host**: bpodpedbpytr3ztavoei-mysql.services.clever-cloud.com
- **Database**: bpodpedbpytr3ztavoei
- **Usuario**: untt7ovn5opdws4y
- **Contraseña**: bX0HCukffFM2nBx4T4h6
- **Port**: 3306

2. **Herramienta de Gestión de Base de Datos**:
Puedes utilizar cualquier herramienta de gestión de bases de datos MySQL, como MySQL Workbench o phpMyAdmin, para administrar la base de datos. Utiliza las credenciales proporcionadas para conectarte a la base de datos en la nube.

## Crear Usuarios

Para crear un nuevo usuario en el sistema, sigue estos pasos:

1. Accede a la página web del sistema.
2. Haz clic en el enlace "Crear Usuario" en la barra de navegación.
3. Completa el formulario con el nombre y el correo electrónico del nuevo usuario.
4. Haz clic en el botón "Crear Usuario" para agregar el nuevo usuario a la base de datos.

## Desplegar el Proyecto

Para desplegar el proyecto en un entorno de producción, sigue estos pasos:

1. **Configuración del Entorno**: 
Asegúrate de tener un entorno de producción adecuado configurado, como un servidor web y un servidor de aplicaciones.

2. **Configuración de la Base de Datos**:
Configura las variables de entorno o los archivos de configuración de la aplicación Flask con las credenciales de la base de datos en la nube.

3. **Ejecución de la Aplicación**:
Ejecuta la aplicación Flask en tu entorno de producción utilizando un servidor WSGI como Gunicorn o uWSGI.

4. **Configuración del Servidor Web**:
Configura el servidor web para que sirva la aplicación Flask y gestione las solicitudes HTTP entrantes.

5. **Pruebas y Monitoreo**:
Realiza pruebas exhaustivas para asegurarte de que la aplicación esté funcionando correctamente en el entorno de producción. Implementa un sistema de monitoreo para supervisar el rendimiento y la disponibilidad de la aplicación.

### Colaboradores y Contexto

Este proyecto fue desarrollado por Johannes Carofilis y Antonio Briones como parte de la materia de Calidad de Software como una práctica académica. Si tienes alguna pregunta o necesitas más ayuda, no dudes en contactar al equipo de desarrollo.
