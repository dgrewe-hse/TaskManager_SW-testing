# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure output is sent straight to terminal (e.g., for logging)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "taskmanager/app/api.py"]
