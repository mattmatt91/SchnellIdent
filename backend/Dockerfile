# Use an official Python runtime as the base image
FROM arm64v8/python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of your application code to the working directory
COPY . /app

# Expose the port your application will run on
EXPOSE 4000

# Set environment variables
ENV NAME backend

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]

