# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Create staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django app
CMD ["gunicorn", "myweb.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000
