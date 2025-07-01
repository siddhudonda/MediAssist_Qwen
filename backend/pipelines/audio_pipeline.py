def transcribe_audio(audio_path):
    model = load_whisper()
    return model.transcribe(audio_path)["text"]
