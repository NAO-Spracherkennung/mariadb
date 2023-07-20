import whisper

model = whisper.load_model("tiny")
print("Model loaded")

def transcribe(filename):

    # Audio laden and auf 30 Sekunden erhöhen
    audio = whisper.load_audio(filename)
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

    return result.text
