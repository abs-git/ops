FROM python:3.10-slim

WORKDIR /app2

RUN pip install --no-cache-dir fastapi uvicorn

COPY fastapi/app2 /app2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]