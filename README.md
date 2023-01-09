### Entorno virtual en python

Un entorno virtual de Python es un ambiente creado con el objetivo de aislar recursos como librerías y entorno de ejecución, del sistema principal o de otros entornos virtuales. 
Lo anterior significa que en el mismo sistema, maquina o computadora, es posible tener instaladas multiples versiones de una misma librería sin crear ningún tipo de conflicto.

# 

### venv

El módulo venv proporciona soporte para crear «entornos virtuales» ligeros con sus propios directorios de ubicación, 
aislados opcionalmente de los directorios de ubicación del sistema. Cada entorno virtual tiene su propio binario 
Python (que coincide con la versión del binario que se utilizó para crear este entorno) 
y puede tener su propio conjunto independiente de paquetes Python instalados en sus directorios de ubicación.

venv es un paquete que viene con Python 3. Python 2 no contiene venv.

Documentacion: https://docs.python.org/es/3.8/library/venv.html

### Comandos para configurar entorno virtual en python con venv

**crear ambiente virtual (se creara una carpeta con el nombre asignado)**

`python -m venv nombredeentornovirtual`

**ingresar a la carpeta "\entorno-virtual\test-entorno-virtual\Scripts\" y activar entorno virtual con comando: 
**

`activate`

**para desactivar entorno virtual utilizar comando :**

`deactivate`

**ver lista de librerias**

`pip list`

**instalar librerias para este proyecto**

`pip install pandas so`

**exportar librerias en archivo requirements.txt**

`pip freeze > requirements.txt`

**instalar librerias de archivo requirements.txt**

`pip install -r requirements.txt`

### Virtualenv

virtualenv es una herramienta para crear entornos Python aislados. Desde Python 3.3, un subconjunto se ha integrado en la biblioteca estándar bajo el módulo venv. 

Documentacion: https://virtualenv.pypa.io/en/latest/

### Comandos para configurar entorno virtual en python con virtualenv

**instalar libreria virtualenv para entornos virtuales en python**

`pip install virtualenv`

**crear ambiente virtual (se creara una carpeta con el nombre asignado)**

`virtualenv nombredeentornovirtual`

**ingresar a la carpeta "\entorno-virtual\test-entorno-virtual\Scripts\" y activar entorno virtual con comando: 
**

`activate`

**para desactivar entorno virtual utilizar comando : **

`deactivate`

**ver lista de librerias**

`pip list`

**instalar librerias para este proyecto**

`pip install pandas so`

**exportar librerias en archivo requirements.txt**

`pip freeze > requirements.txt`

**instalar librerias de archivo requirements.txt**

`pip install -r requirements.txt`

