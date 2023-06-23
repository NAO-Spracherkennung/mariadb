from flask import Flask, request
import whisper
import os

MODEL = os.environ['WHISPER_MODEL']


def setup():

    print("Downloading whisper model..."+MODEL)

    # transcribes an empty audio file to download the model instead of downloading it on the first request
    model = whisper.load_model(MODEL)
    whisper.transcribe(model, "setup.m4a")

    print("Setup finished")

    return "OK"


setup()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def transcribe():

    # Audiodatei aus Request laden
    file = request.files['file']

    # Audiodatei zwischenspeichern
    f = open("audio", 'wb')
    f.write(file.read())
    f.close()

    model = whisper.load_model(MODEL)

    # Audio laden and auf 30 Sekunden erhöhen
    audio = whisper.load_audio("audio")
    audio = whisper.pad_or_trim(audio)

    # Log-Mel Spektrogramm erstellen
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Decoder-Optionen festlegen
    options = whisper.DecodingOptions(
        task="transcribe",
        language="de",
        fp16=False,
        without_timestamps=True)

    # Transkription durchführen
    result = whisper.decode(
        model=model,
        mel=mel,
        options=options)

    print("Transkribierter Text:  "+result.text)

    return result.text
