FROM python:3.14-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/
    
RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]