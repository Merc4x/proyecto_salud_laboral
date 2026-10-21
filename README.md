<div align="center">
  <h1>Soluciones Administrativas en Salud Laboral</h1>
  <p><b>Plataforma web integral para asesoría y gestión en Seguridad y Salud en el Trabajo (SG-SST)</b></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
    <img src="https://img.shields.io/badge/Frontend-HTML5%20%7C%20CSS3%20%7C%20JS-E34F26?style=flat-square" alt="Frontend" />
    <img src="https://img.shields.io/badge/Arquitectura-Modular%20Jinja2-B41717?style=flat-square" alt="Jinja2" />
  </p>
</div>

---

## Descripción

Aplicación web desarrollada para la difusión, gestión y contratación de servicios especializados en Seguridad y Salud en el Trabajo (SG-SST). La plataforma conecta a empresas, pymes y contratistas con servicios profesionales de consultoría legal y técnica, auditorías preventivas y programas de capacitación laboral.

---

## Características Principales

- **Gestión de Servicios SG-SST:** Catálogo interactivo de servicios de consultoría, diseño e implementación del Sistema de Gestión de Seguridad y Salud en el Trabajo bajo normativa legal vigente.
- **Auditorías y Capacitaciones:** Sección dedicada a programas de formación, inspecciones y preparación de empresas para auditorías regulatorias.
- **Canal Directo de Contacto:** Integración fluida con canales de mensajería (WhatsApp Business) para agendamiento rápido de asesorías y cotizaciones.
- **Arquitectura Modular y Responsiva:** Backend ligero en Python con Flask y motor de plantillas Jinja2, estructurado con hojas de estilo personalizadas y diseño adaptativo para dispositivos móviles y de escritorio.

---

## Stack Tecnológico

| Componente | Tecnología |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3 personalizado, JavaScript, FontAwesome |
| **Motor de Plantillas** | Jinja2 |
| **Despliegue / Servidor** | WSGI / Werkzeug |

---

## Instalación y Ejecución Local

### Prerrequisitos
- Python 3.10 o superior instalado.

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Merc4x/proyecto_salud_laboral.git
   cd proyecto_salud_laboral
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Acceder en el navegador:**
   Ingresa a [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Estructura del Proyecto

```text
proyecto_salud_laboral/
├── static/
│   ├── css/
│   │   └── style.css            # Estilos personalizados y diseño responsivo
│   └── img/                    # Banners, logotipos y recursos gráficos
├── templates/
│   ├── base.html               # Plantilla maestra (Layout general)
│   ├── index.html              # Página de inicio
│   ├── nosotros.html           # Información institucional y misión
│   ├── servicios.html          # Detalle de servicios SG-SST
│   └── capacitaciones.html     # Programas y auditorías
├── app.py                      # Enrutamiento y servidor Flask
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación técnica
```

---

## Autor

Desarrollado por **Alejandro Mercado** ([@Merc4x](https://github.com/Merc4x)).
