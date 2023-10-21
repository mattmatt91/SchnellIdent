FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade -r requirements.txt

EXPOSE 3000

ENV NAME backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]
