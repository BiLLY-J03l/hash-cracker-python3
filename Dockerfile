FROM python:3.13-slim

WORKDIR /app

COPY . /app

ENTRYPOINT ["python", "hash_cracker.py"]
