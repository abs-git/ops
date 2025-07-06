FROM python:3.10-slim

WORKDIR /app1

RUN pip install --no-cache-dir fastapi uvicorn

COPY fastapi/app1 /app1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]