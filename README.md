# devops-proyecto-final
Proyecto final de la materia DevOps: Agilizando el Despliegue Continuo de Aplicaciones

## Como ejecutar el proyecto:

1. En el archivo **gunicorn.conf.py** cambie la configuración de arranque (por ejemplo puerto, archivos de logs, etc.).
2. Ejecute el siguiente comando:

``` bash
# Para ejecutar en modo PRD
gunicorn -c gunicorn.conf.py main:app

# Para ejecutar en modo Test
export TEST_ENV=True && gunicorn -c gunicorn.conf.py main:app
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

## Como ejecutar con Docker

``` bash
docker build -t devops-proyecto-final-img:latest .

docker run -it -d --name devops-proyecto-final -p 5001:5001 -e DATABASE_URL=postgresql://postgres:users12345@192.168.1.13:5432/postgres -e NEW_RELIC_LICENSE_KEY=d7a91e42c315038552618a364774cc30FFFFNRAL devops-proyecto-final-img:latest
``` 

Para detener los servicios:

``` bash
docker stop devops-proyecto-final && docker rm devops-proyecto-final

docker rmi devops-proyecto-final-img
``` 
User: postgres
postgres123456*+