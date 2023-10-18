FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 3010

ENV NAME hardware

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3010", "--reload"]
