FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
