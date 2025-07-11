import openai
import io
import os
from dotenv import load_dotenv

# used to extract text from audio files using OpenAI Whisper
load_dotenv()  # Load variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

async def transcribe_audio(audio_file):
    contents = await audio_file.read()
    audio_bytes = io.BytesIO(contents)
    audio_bytes.name = audio_file.filename  # Important for OpenAI to detect .mp3
    transcript = openai.Audio.transcribe("whisper-1", audio_bytes)
    return transcript["text"]
