FROM python:3.14-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=0
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
COPY . /app/
    
RUN pip install -r requirements.txt

EXPOSE 5001

#CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]

##Confguración New Relic
ENV NEW_RELIC_APP_NAME="devops-proyecto-final-aws"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LOG_LEVEL=info
ENV NEW_RELIC_CONFIG_FILE=newrelic/newrelic.ini

ENTRYPOINT ["newrelic-admin", "run-program", "gunicorn", "-c", "gunicorn.conf.py", "main:app"]