FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install pyftpdlib

CMD ["python3", "ftp_honeypot.py"]
