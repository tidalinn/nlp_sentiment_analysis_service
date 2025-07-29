FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y make && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/requirements-base.txt /app/requirements/
RUN pip install --no-cache-dir -r requirements/requirements-base.txt

COPY . .
