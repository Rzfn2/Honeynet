FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install paramiko

CMD ["python3", "ssh_honeypot.py"]
