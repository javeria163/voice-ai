# 🎤 Real-Time Voice AI Assistant

A sub-500ms latency voice AI — speak to it and it responds instantly with a human-like voice. Works in browser and on a real phone number.

## 🎯 Demo

### 🌐 Web Interface (Everyone)
- Clone the repo and run locally
- Open browser → click the orb → speak → AI responds instantly

### 📞 Live Phone Demo (US Residents only)
- Call **+1 (984) 372-1335**
- Talk to the AI directly on a real phone call!
- *Note: Currently available for US callers only*

## ✨ Features
- 🎤 **Real-time speech recognition** — hears you instantly
- 🧠 **AI brain** — Groq (Llama 3.3 70B) processes in milliseconds
- 🔊 **Human-like voice** — ElevenLabs TTS
- 💬 **Conversation memory** — remembers context
- 📞 **Phone ready** — Twilio integration for real calls
- ⚡ **Sub-500ms** — end-to-end latency

## 🛠️ Tech Stack
- **Groq API** (Llama 3.3 70B) — AI responses
- **ElevenLabs** — human voice synthesis
- **Twilio** — phone call integration
- **FastAPI** — backend server
- **Web Speech API** — browser microphone

## 🚀 Run It Yourself

Install dependencies:
```bash
pip install -r requirements.txt
```

Start the server:
```bash
python main.py
```

Open browser:
http://localhost:8000

## 🔑 Setup
Create a `.env` file:
GROQ_API_KEY=your_groq_key

ELEVENLABS_API_KEY=your_elevenlabs_key

TWILIO_ACCOUNT_SID=your_twilio_sid

TWILIO_AUTH_TOKEN=your_twilio_token

TWILIO_PHONE_NUMBER=+19843721335

BASE_URL=your_ngrok_url

## 💡 Inspired By
- Hume AI
- Retell AI
- ElevenLabs Conversational AI