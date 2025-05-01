# FROM python:3.10-slim-buster
# WORKDIR /app
# COPY . /app

# RUN apt update -y && apt install awscli -y

# RUN apt-get update && pip install -r requirements.txt
# CMD ["python3", "app.py"]





# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container
COPY . /app/

# Set environment variables (optional but useful)
# ENV MONGO_DB_URL="your_mongo_db_connection"
# ENV MLFLOW_TRACKING_URI="your_mlflow_uri"

# Expose the port the app runs on (if needed for services like Flask)
EXPOSE 5000

# Command to run when the container starts
CMD ["python", "main.py"]
