Proyecto de Registro de Eventos en Django

Este es un proyecto web simple desarrollado en Django que permite a los usuarios registrar eventos y añadir participantes a cada evento. El proyecto fue creado como un ejercicio para demostrar el manejo de formularios, FormSets, validación de datos y plantillas reutilizables en Django.

Características Principales

    Registro de Eventos: Formulario para crear un nuevo evento con nombre, fecha, ubicación y descripción.

    Gestión de Participantes: Posibilidad de añadir uno o más participantes (nombre y correo) al evento en el mismo formulario de registro.

    Validación de Datos:

        El nombre del evento no puede superar los 100 caracteres.

        La fecha del evento debe ser una fecha futura.

        Los campos obligatorios son validados para evitar envíos vacíos.

    Plantillas Reutilizables: Uso de un sistema de plantillas base con bloques para mantener el código DRY (Don't Repeat Yourself).

hola

Requisitos

    Python 3.8+

    Django 5.0+

    (Opcional) Git para clonar el repositorio.

Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

    Clona el repositorio (si aplica):
    Bash

git clone [URL-DEL-REPOSITORIO]
cd [NOMBRE-DEL-PROYECTO]

Crea y activa un entorno virtual:
Bash

# En Windows
python -m venv venv
.\venv\Scripts\activate

# En macOS / Linux
python3 -m venv venv
source venv/bin/activate

Instala las dependencias:
(Asegúrate de tener un archivo requirements.txt en tu proyecto)
Bash

pip install -r requirements.txt

Si no tienes un requirements.txt, instala Django manualmente:
Bash

pip install django

Aplica las migraciones:
Esto creará las tablas necesarias en la base de datos.
Bash

python manage.py migrate

Inicia el servidor de desarrollo:
Bash

    python manage.py runserver

    Abre tu navegador y ve a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

División del Trabajo


    Desarrolladores(Backend):

        Configuración del proyecto y la base de datos (models.py).

        Creación de los formularios y FormSets (forms.py).

        Implementación de la lógica de validación personalizada.

    Desarrolladores (Frontend y Vistas):

        Desarrollo de la lógica de las vistas para manejar las solicitudes GET y POST (views.py).

        Creación de las plantillas HTML y la estructura del frontend.

        Configuración de las rutas de la aplicación (urls.py).
