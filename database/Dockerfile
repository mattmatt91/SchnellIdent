FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY . /app

RUN pip install  -r requirements.txt

EXPOSE 3040

ENV NAME database


# CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3040"]


