# 💍 Invitación Web Interactiva

Una aplicación web full-stack diseñada como una invitación de boda digital con temática sutil de *The Legend of Zelda*. Este proyecto permite a los invitados visualizar los detalles del evento, interactuar con la interfaz y confirmar su asistencia mediante un sistema automatizado conectado a una base de datos.

## ✨ Características Principales

* **UI/UX Temático:** Interfaz elegante en tonos verde y dorado, tipografías clásicas (`Cinzel` y `Cormorant Garamond`) y detalles visuales referentes a la saga de Zelda (Trifuerza, botones personalizados).
* **Efectos de Partículas:** Integración de `particles.js` configurado a medida para simular polvo mágico o "Hadas de Hyrule" flotando en el fondo (sin líneas conectoras para un look más limpio).
* **Audio Inmersivo:** Reproductor web integrado que permite al invitado activar/pausar *Zelda's Lullaby* de fondo, respetando las políticas de *autoplay* de los navegadores modernos mediante un botón flotante (Toggle).
* **Sistema de Modales (SPA):** Navegación fluida de una sola página utilizando ventanas modales para mostrar:
  * **Ubicaciones:** Mapas embebidos para la iglesia y el salón.
  * **Mesa de Regalos:** Enlace de redirección externa (Liverpool).
  * **Confirmación:** Formulario de captura de datos.
* **Sistema de Registro Seguro:** Backend configurado para recibir peticiones `POST` del formulario, con lógica de validación previa que consulta la base de datos para evitar registros duplicados del mismo invitado.

## 🛠️ Tecnologías Utilizadas

**Frontend:**
* HTML5 / CSS3 (Diseño responsivo, Flexbox, variables CSS, `z-index` layering).
* JavaScript (Vanilla JS para control del DOM, manipulación de modales y control del objeto `Audio`).
* `particles.js` (Librería externa por CDN).

**Backend & Datos:**
* **Python 3:** Lenguaje principal de la lógica del servidor.
* **Flask:** Micro-framework web utilizado para el enrutamiento (`@app.route`) y renderizado de vistas (`render_template`).
* **SQLite:** Base de datos relacional ligera (`boda.db`) para el almacenamiento persistente de los invitados.

## Arquitectura de Directorios
El proyecto sigue la estructura estándar de Flask:

```text
BODAZELDA/
│
├── app.py                 # Script principal del servidor Flask y rutas
├── boda.db                # Base de datos SQLite (Tabla: invitados)
│
├── templates/             
│   └── index.html         # Estructura principal, modales y reproductor
│
└── static/                # Archivos estáticos públicos
    ├── index.css          # Hojas de estilo y variables
    ├── index.js           # Lógica del cliente y configuración de partículas
    ├── lullaby.mp3        # Pista de audio ambiental
    └── img/
        ├── esquina.png    # Ornamentos de las esquinas
        └── trifuerza.png  # Logotipo central
