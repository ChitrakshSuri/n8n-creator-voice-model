# 🎙️ n8n-creator-voice-model

An intelligent voice assistant to **ask questions about your n8n workflows** — using your **voice**!

Powered by:
- OpenAI GPT-4 for contextual answers  
- OpenAI Whisper for audio transcription  
- ElevenLabs for voice response  

---

## 🧠 What It Does

Upload an `.mp3` file containing your voice question and receive:
- The **transcribed text**
- A smart **GPT-4 response**, with reference to your `workflow.json`
- A **spoken answer** as an `.mp3` file

---

## 📁 Folder Structure

```
n8n-creator-voice-model/
├── backend/
│   ├── main.py                ← FastAPI app
│   ├── workflow.json          ← n8n workflow data (used by GPT)
│   └── services/
│       ├── whisper.py         ← Converts speech to text using OpenAI Whisper
│       ├── llm.py             ← Queries GPT-4 with workflow context
│       └── tts.py             ← Converts text response to audio using ElevenLabs
├── frontend/
│   └── static/                ← Audio responses are saved here
├── .env                       ← API keys (not committed)
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/n8n-creator-voice-model.git
cd n8n-creator-voice-model
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your environment variables

Create a `.env` file at the root:

```env
OPENAI_API_KEY=your_openai_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key
VOICE_ID=your_elevenlabs_voice_id
```

## ▶️ Run the App

```bash
uvicorn backend.main:app --reload
```

Then open your browser and go to:
📍 http://localhost:8000/docs

You'll see Swagger UI to test the `/ask` endpoint.

---

## 🧪 How to Test with Postman

**POST** `/ask`  
**Body Type:** form-data

| Key   | Type | Value         |
|-------|------|---------------|
| audio | File | yourfile.mp3  |

You'll get a JSON response like:

```json
{
  "text": "This is your GPT-4 generated answer...",
  "audio_url": "/static/xyz123.mp3"
}
```

Click the `audio_url` to hear the spoken reply.

---

## 📘 About workflow.json

This file provides context to GPT-4 about your n8n workflow.

Structure:

```json
{
  "name": "Send Email on Form Submission",
  "trigger": "Webhook",
  "steps": [
    "Receive form data",
    "Format email",
    "Send via SMTP"
  ]
}
```

You can customize this with your own workflow info.

---

## 📦 .gitignore Suggestions

You should NOT commit:

```gitignore
__pycache__/
.env
```

---

## 🧠 Tech Stack

- FastAPI (Python backend)
- OpenAI GPT-4 (ChatCompletion API)
- OpenAI Whisper (Audio transcription)
- ElevenLabs TTS API
- Postman or Swagger UI for testing

---

## 🧰 Bonus Tip 🔒

If you forget the run command, just use this:

```bash
uvicorn backend.main:app --reload
```

---

## 👨‍💻 Author

**Chitraksh Suri**  
AI Agent Intern @ Dreamable  
🌐 [LinkedIn](https://linkedin.com/in/chitraksh-suri) • 🧑‍💻 [GitHub](https://github.com/chitrakshsuri)

---

## 📜 License

MIT – Free to use, modify, and share.