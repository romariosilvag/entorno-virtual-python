"""
Virtualenv

virtualenv es una herramienta para crear entornos Python aislados. Desde Python 3.3, un subconjunto se ha integrado en la biblioteca estándar bajo el módulo venv. 

Documentacion: https://virtualenv.pypa.io/en/latest/

Comandos para configurar entorno virtual en python con virtualenv

# instalar libreria virtualenv para entornos virtuales en python
pip install virtualenv

# crear ambiente virtual (se creara una carpeta con el nombre asignado)
virtualenv nombredeentornovirtual

# ingresar a la carpeta "\entorno-virtual\test-entorno-virtual\Scripts\" y activar entorno virtual con comando: 
activate

# para desactivar entorno virtual utilizar comando : 
deactivate

# ver lista de librerias
pip list

# instalar librerias para este proyecto
pip install pandas so

# exportar librerias en archivo requirements.txt
pip freeze > requirements.txt

# instalar librerias de archivo requirements.txt
pip install -r requirements.txt


"""

print("Hola mundo!")