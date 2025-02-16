# Validación de acceso

Este proyecto es una API RESTful hecha con Flask-RESTx para gestionar una autorizacion de usuarios en base a un dni. Flask-RESTx es una extensión de Flask que facilita la creación de APIs RESTful. Puedes encontrar más información en la [documentación de Flask-RESTx](https://flask-restx.readthedocs.io/).

## Requisitos Previos

1. Tener instalado [Docker](https://www.docker.com/)

## Instalación
Para construir y levantar el proyecto, ejecuta los siguientes comandos:

```sh
docker compose build
docker compose up
```

Primero, verifica si las tablas del `init.sql` se crearon automáticamente. Si no es así, ejecuta las queries del archivo `init.sql` para crear las tablas necesarias en la base de datos.

## Probar el Funcionamiento

Entrar a la página [http://localhost:5001](http://localhost:5001) para acceder a la documentación de Swagger.

## Endpoints

### Usuarios

- `POST /users/acceso`: Consulta el accesso de un usuario utilizando el dni.


