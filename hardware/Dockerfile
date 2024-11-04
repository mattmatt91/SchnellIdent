# Use the official Python image as a base image
FROM python:3.9-slim-buster


ARG REACT_APP_IP_BACKEND
ENV REACT_APP_IP_BACKEND=${REACT_APP_IP_BACKEND}

ARG REACT_APP_IP_DAQ
ENV REACT_APP_IP_DAQ=${REACT_APP_IP_DAQ}

ARG REACT_APP_PORT_DAQ
ENV REACT_APP_PORT_DAQ=${REACT_APP_PORT_DAQ}




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
