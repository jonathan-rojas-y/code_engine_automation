FROM python:3.8

WORKDIR /app

COPY src /app

RUN pip install ibm-cos-sdk

CMD ["python", "main.py"]
