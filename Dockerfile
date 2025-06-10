## Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (for psycopg2 or Pillow support)
RUN apt-get update -o Acquire::http::Pipeline-Depth=0 && \
    apt-get install -y apt-transport-https ca-certificates && \
    apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create staticfiles directory and collect static files
RUN mkdir -p /app/staticfiles && \
    python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "myweb.wsgi:application", "--bind", "0.0.0.0:8000"]

