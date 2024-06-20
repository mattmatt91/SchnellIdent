# Use the official Python image as a base image
FROM arm64v8/python:3.9-slim

# Install system dependencies and Git
#RUN apt update && apt install -y git

# Create a directory for the application
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt



# Copy the rest of the application code
COPY . /app/

# RUN apt-get update && apt-get install -y wget unzip
# RUN chmod +x install_pig.sh
# RUN ./install_pig.sh

# Expose the desired port
EXPOSE 3010

# Set environment variables
ENV NAME hardware

# Define the command to start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3010", "--reload"]
