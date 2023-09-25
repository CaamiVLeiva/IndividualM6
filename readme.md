# Proyecto de Registro y Autenticación en Django

## Descripción
Este proyecto se centra en la implementación de un sistema de registro y autenticación en una aplicación web Django. Los usuarios pueden registrarse, iniciar sesión y acceder a contenido personalizado después de iniciar sesión.


## Requisitos
- Python 3.x
- Django
- Paquetes adicionales según lo definido en `requirements.txt`

## Instalación
1. Clona este repositorio en tu máquina local: `git clone https://github.com/tuusuario/tuproyecto.git`
2. Crea un entorno virtual: `python3 -m venv myenv`
3. Activa el entorno virtual: `source myenv/bin/activate` (en Windows, usa `myenv\Scripts\activate`)
4. Instala las dependencias: `pip install -r requirements.txt`
5. Aplica las migraciones: `python manage.py migrate`
6. Ejecuta el servidor: `python manage.py runserver`

## Configuración
- Asegúrate de configurar la base de datos en `settings.py`.
- Define la clave secreta y las configuraciones de seguridad según sea necesario.

## Uso
- Accede a la página de inicio y registra una nueva cuenta.
- Inicia sesión con la cuenta de administrador:
  - Nombre de usuario: admin
  - Contraseña: admin
- O inicia sesión con una cuenta de usuario de prueba:
  - Nombre de usuario: usuario1
  - Contraseña: contraseña

## Funcionalidad
- Registro de usuarios.
- Inicio de sesión y cierre de sesión.
- Mensaje de bienvenida personalizado después del inicio de sesión.

## Estructura de Directorios
- `onlinecourse/`: Aplicación principal.
- `templates/`: Plantillas HTML.
- `static/`: Archivos estáticos (CSS, JS, imágenes).
