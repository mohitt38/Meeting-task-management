# stt.py
import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # small & fast
    result = model.transcribe(audio_path)
    return result["text"]