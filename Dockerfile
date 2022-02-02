FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./src/ /app/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
