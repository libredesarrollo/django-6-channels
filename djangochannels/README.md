# Proyecto de Ejemplo con Django Channels

Este proyecto es un ejemplo práctico para aprender a utilizar Django Channels y WebSockets para crear aplicaciones en tiempo real con Django.

## Descripción

A través de este proyecto, podrás comprender los conceptos fundamentales de Django Channels, incluyendo:

-   Configuración de un servidor ASGI.
-   Creación de Consumers para manejar conexiones WebSocket.
-   Gestión de canales y grupos.
-   Comunicación en tiempo real entre el cliente y el servidor.
-   Integración con el ORM de Django y la autenticación.

El proyecto incluye una aplicación de chat simple y una aplicación de alertas en tiempo real.

## Configuración y Puesta en Marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### Prerrequisitos

-   Python 3.9 o superior
-   Redis

### 1. Clona el repositorio

```bash
git clone <URL-DEL-REPOSITORIO>
cd djangochannels
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instala las dependencias

Todas las dependencias necesarias se encuentran en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Realiza las migraciones de la base de datos

```bash
python manage.py migrate
```

### 5. Inicia el servidor de desarrollo

Para que Django Channels funcione, necesitas ejecutar el servidor ASGI en lugar del servidor de desarrollo WSGI tradicional.

```bash
daphne -p 8001 djangochannels.asgi:application
```
O también puedes usar el servidor de desarrollo de Django que soporta ASGI:
```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000`.

## ¿Quieres aprender más sobre Django?

Si estás interesado en profundizar tus conocimientos en Django y desarrollo web con Python, te invito a revisar mis recursos educativos:

[![Primeros Pasos con Django](https://www.desarrollolibre.net/public/images/libros/primeros-pasos-django-v2-cover.png)](https://www.desarrollolibre.net/libros/primeros-pasos-django)

### Libros

-   **[Primeros Pasos con Django](https://www.desarrollolibre.net/libros/primeros-pasos-django)**: Una guía completa para iniciarte en el desarrollo de aplicaciones web con el framework Django.

### Cursos

-   **[Curso de Django](https://www.desarrollolibre.net/blog/python/curso-django)**: Aprende a crear aplicaciones web robustas y escalables desde cero con Django.

---
*Proyecto creado por [desarrollolibre.net](https://www.desarrollolibre.net)*
