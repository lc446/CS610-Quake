FROM python:3.12-slim

RUN apt update -y
RUN apt install qstat -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
