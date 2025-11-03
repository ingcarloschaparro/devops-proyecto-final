# devops-proyecto-final
Proyecto final de la materia DevOps: Agilizando el Despliegue Continuo de Aplicaciones

## Como ejecutar el proyecto:

1. En el archivo **gunicorn.conf.py** cambie la configuración de arranque (por ejemplo puerto, archivos de logs, etc.).
2. Ejecute el siguiente comando:

``` bash
gunicorn -c gunicorn.conf.py main:app
```

## Como ejecutar las pruebas

### Pruebas unitarias

``` bash
pytest --cov=api -x --cov-report=html --cov-fail-under=90
```

### Verificaciones estáticas de código

``` bash
flake8 **/*.py
```

### Pruebas de integración con Newman

``` bash
newman run tests/Uniandes_DevOps_ProyectoFinal.postman_collection.json -r cli,junit --reporter-junit-export postman_results.xml
```


User: postgres
postgres123456*+