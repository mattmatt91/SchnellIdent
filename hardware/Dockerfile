FROM arm32v7/python:3.9-slim

# Install Git using apt
RUN apt update && apt install -y git

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt 
RUN git clone https://github.com/mccdaq/daqhats.git \
    && cd /app/daqhats \
    && ./install.sh

EXPOSE 3010

ENV NAME hardware

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3010", "--reload"]
