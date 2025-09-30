# Sistema de Registro de Eventos

Este es un proyecto web desarrollado en Django que permite registrar eventos y gestionar participantes asociados. El proyecto demuestra el uso avanzado de formularios en Django, incluyendo FormSets inline, validaciones personalizadas y manejo de transacciones.

## Características Principales

###  **Registro de Eventos**
- Formulario único para crear eventos con nombre, fecha y ubicación
- Validación automática de fecha futura
- Prevención de eventos duplicados (mismo nombre y fecha)
- Ubicación opcional

###  **Gestión de Participantes**
- Formulario integrado que permite añadir múltiples participantes por evento
- Hasta 3 participantes por defecto (configurable)
- Validación de formato de correo electrónico
- Asociación automática de participantes al evento creado

###  **Validaciones Implementadas**
- **Fecha futura**: Los eventos deben programarse para fechas posteriores al día actual
- **Unicidad**: No se permiten eventos con el mismo nombre en la misma fecha
- **Correo válido**: Los participantes deben tener correos con formato correcto
- **Campos obligatorios**: Validación de todos los campos requeridos

###  **Características Técnicas**
- **FormSets Inline**: Manejo avanzado de formularios relacionados
- **Transacciones Atómicas**: Garantía de integridad de datos
- **Mensajes de Usuario**: Feedback visual de operaciones exitosas
- **Plantillas Base**: Sistema de herencia de plantillas DRY

## Requisitos del Sistema

- **Python**: 3.8 o superior
- **Django**: 5.2.6 (especificado en requirements.txt)
- **Base de datos**: SQLite (por defecto) o cualquier base compatible con Django
- **Git**: Opcional, para control de versiones

## Instalación y Configuración

### 1. Preparar el Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
# Instalar Django y dependencias
pip install -r requirements.txt
```

### 3. Configurar Base de Datos

```bash
# Aplicar migraciones
python manage.py migrate
```

### 4. Ejecutar el Servidor

```bash
# Iniciar servidor de desarrollo
python manage.py runserver
```

### 5. Acceder a la Aplicación

Abre tu navegador web y ve a: **http://127.0.0.1:8000/**

El formulario de registro de eventos estará disponible en la página principal.

## Acceso al Panel de Administrador

Para gestionar los datos directamente, puedes usar el panel de administrador de Django.

1.  **Accede a la URL** del administrador:
    [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

2.  **Inicia sesión** con las siguientes credenciales de prueba:
    - **Usuario**: `admin`
    - **Contraseña**: `admin`

*Nota: Si estas credenciales no funcionan, puedes crear tu propio superusuario ejecutando el comando:* `python manage.py createsuperuser`

## Arquitectura del Proyecto

###  **Modelo de Datos**
- **Evento**: Entidad principal con nombre, fecha y ubicación opcional
- **Participante**: Relacionado con Evento mediante Foreign Key con CASCADE
- Relación uno-a-muchos entre Evento y Participante

###  **Formularios**
- **EventoForm**: ModelForm con validaciones personalizadas de fecha y unicidad
- **ParticipanteForm**: ModelForm para participantes con validación de correo
- **FormSet Inline**: Manejo integrado de múltiples participantes por evento

###  **Vista Principal**
- Función `crear_evento` que maneja tanto GET como POST
- Uso de `inlineformset_factory` para participantes
- Manejo de transacciones para integridad de datos
- Sistema de mensajes para feedback al usuario

###  **Plantillas**
- Sistema de herencia de plantillas con `base.html`
- Formulario integrado en `event_form.html`
- Diseño responsivo y user-friendly

###  **URLs**
- Ruta raíz (`/`) apunta directamente al formulario de creación de eventos
- Integración con el sistema de URLs de Django

## Uso de la Aplicación

### Crear un Evento

1. **Accede** a la aplicación en tu navegador
2. **Completa** el formulario de evento:
   - **Nombre**: Nombre único del evento (máx. 100 caracteres)
   - **Fecha**: Selecciona una fecha futura usando el selector de fecha
   - **Ubicación**: Especifica dónde se realizará el evento (opcional)
3. **Añade participantes**:
   - Completa al menos un participante con nombre y correo válido
   - Puedes añadir hasta 3 participantes adicionales
   - El correo debe tener formato válido (@ dominio)
4. **Envía** el formulario
5. **Verifica** el mensaje de confirmación

### Características del Formulario

- **Validación en tiempo real** de fechas futuras
- **Prevención de duplicados** de eventos
- **Formato automático** de campos de fecha y correo
- **Transacción atómica** que garantiza que si algo falla, no se guarda nada
- **Mensajes de éxito** para confirmar el registro

## Estructura del Proyecto

```
registroDeEventos/
├── registroDeEventos/      # Configuración del proyecto Django
│   ├── settings.py         # Configuración principal
│   ├── urls.py             # Rutas principales
│   └── ...
├── registrarEventos/       # Aplicación principal
│   ├── models.py           # Modelos de datos (Evento, Participante)
│   ├── forms.py            # Formularios y validaciones
│   ├── views.py            # Lógica de la vista crear_evento
│   ├── urls.py             # Rutas de la aplicación
│   ├── templates/          # Plantillas HTML
│   ├── static/             # Archivos estáticos (CSS, JS, imágenes)
│   └── migrations/         # Migraciones de base de datos
├── requirements.txt        # Dependencias de Python
├── manage.py               # Script de gestión de Django
└── README.md               # Este archivo
```

## Tecnologías Utilizadas

- **Django 5.2.6**: Framework web principal
- **SQLite**: Base de datos por defecto
- **Python 3.8+**: Lenguaje de programación
- **HTML5/CSS3**: Interfaz de usuario
- **FormSets**: Para manejo de múltiples participantes
- **Bootstrap**: Framework CSS (si está incluido en templates)
