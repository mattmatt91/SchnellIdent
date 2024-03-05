FROM arm64v8/python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install  --no-cache-dir --upgrade -r requirements.txt

EXPOSE 4000

ENV NAME backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]
