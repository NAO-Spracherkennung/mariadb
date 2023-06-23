# syntax=docker/dockerfile:1

FROM python:3.9.17-slim-bullseye

ENV WHISPER_MODEL="base"

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install git -y
RUN apt-get install -y ffmpeg

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]