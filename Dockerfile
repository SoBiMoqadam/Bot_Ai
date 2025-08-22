FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY main.py .
COPY env .


RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


ENV PYTHONUNBUFFERED=1


CMD ["python", "main.py"]
