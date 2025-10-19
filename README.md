# devops-proyecto-final
Proyecto final de la materia DevOps: Agilizando el Despliegue Continuo de Aplicaciones

## Como ejecutar el proyecto:

1. En el archivo **gunicorn.conf.py** cambie la configuración de arranque (por ejemplo puerto, archivos de logs, etc.).
2. Ejecute el siguiente comando:

``` bash
gunicorn -c gunicorn.conf.py main:app
```


User: postgres
postgres123456*+