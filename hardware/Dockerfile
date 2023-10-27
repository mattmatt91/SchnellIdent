FROM arm32v7/python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 3010

ENV NAME hardware

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3010", "--reload"]
