FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Put src contents under /app/src so main.py is at /app/src/main.py (and api/ is there too)
COPY src/ ./src/
COPY frontend/ ./frontend/

WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
