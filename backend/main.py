from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
from backend.services.llm import ask_llm
from backend.services.whisper import transcribe_audio
from backend.services.tts import text_to_speech
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
# Handles audio upload, transcribes it, asks GPT about the n8n workflow, and returns text + voice response


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/ask")
async def ask_question(audio: UploadFile = File(...)):
    try:
        print("Uploaded file:", audio.filename)
        print("Type of audio:", type(audio))
        if not audio.filename.endswith(".mp3"):
            return JSONResponse(status_code=400, content={"error": "Only .mp3 files are supported"})
        
        workflow = json.load(open("backend/workflow.json"))
        audio_text = await transcribe_audio(audio)
        answer = await ask_llm(audio_text, workflow)
        audio_response = await text_to_speech(answer)
        return {"text": answer, "audio_url": audio_response}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
