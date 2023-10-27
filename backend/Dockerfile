FROM arm32v7/python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade -r requirements.txt

EXPOSE 3000

ENV NAME backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]
