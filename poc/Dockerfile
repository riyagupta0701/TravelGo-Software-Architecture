FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# make a copy the application
COPY . /app

ENV PYTHONUNBUFFERED=1 FLASK_ENV=production

# show the ports used by your services
EXPOSE 5000 5001 5002 5003 5004 5005 5008

# will be overridden by docker-compose
CMD ["python", "api_gateway.py"]
