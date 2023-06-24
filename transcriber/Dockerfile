FROM python:3.9.17-slim-bullseye

ENV WHISPER_MODEL="base"

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y git ffmpeg curl && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
