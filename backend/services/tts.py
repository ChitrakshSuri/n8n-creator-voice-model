import requests

ELEVEN_API_KEY = "sk_59085251ad79ef3d19af8fa886d084f859b5e9a1857c1859"
VOICE_ID = "zT03pEAEi0VHKciJODfn"

async def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    res = requests.post(url, headers=headers, json=data)
    with open("response.mp3", "wb") as f:
        f.write(res.content)
    return "/path/to/response.mp3"
