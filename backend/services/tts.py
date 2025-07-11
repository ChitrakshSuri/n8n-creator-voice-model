import requests
import uuid
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

async def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"  # VERY IMPORTANT
    }
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)

    # Make sure the response is valid
    if response.status_code != 200:
        raise Exception(f"ElevenLabs Error: {response.text}")

    # Save with a unique filename
    filename = f"{uuid.uuid4().hex}.mp3"
    output_path = Path("static") / filename
    with open(output_path, "wb") as f:
        f.write(response.content)

    return f"/static/{filename}"
