# pokedex

Pasos para ejecutar el proyecto en Docker:
## Paso 1:
Descargar el repositorio e ingresar al directorio del proyecto

## Paso 2:
Compilar la imagen: docker build -t img-pokedex .

## Paso 3:
Ejecutar el contenedor: docker run -d -p 5000:5000 img-pokedex

## -----------------------------------------------

Pasos para ejecutar el proyecto en Local:
## Paso 1:
Descargar el repositorio: git clone <URL del repositorio>

## Paso 2:
Crear entorno virtual en python: python -m venv venv

## Paso 3:
Activar el entorno virtual: .\venv\Scripts\activate

## Paso 4:
Instalar dependencias: Entrar al directorio del repositorio: pip install -r requirements

## Paso 4:
Ejecutar el proyecto: flask run -h 0.0.0.0 -p 5000

## Paso 5:
Comrpobar si el servicio esta ejecutandose: http://localhost:5000/ping

