import os
import base64
from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from twilio.twiml.voice_response import VoiceResponse, Gather, Play
from ai_engine import get_ai_response, reset_conversation
from tts_engine import text_to_speech
from dotenv import load_dotenv
import tempfile

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")

@app.post("/clear")
async def clear():
    reset_conversation()
    return {"status": "cleared"}
@app.post("/incoming-call")
async def incoming_call(request: Request):
    reset_conversation()
    response = VoiceResponse()
    gather = Gather(
        input="speech",
        action="/process-speech",
        method="POST",
        speech_timeout="auto",
        language="en-US"
    )
    gather.say("Hello! I am your AI assistant. How can I help you today?")
    response.append(gather)
    return Response(content=str(response), media_type="application/xml")

@app.post("/process-speech")
async def process_speech(request: Request):
    form_data = await request.form()
    user_speech = form_data.get("SpeechResult", "")
    
    print(f"📞 Caller said: {user_speech}")
    
    if not user_speech:
        response = VoiceResponse()
        gather = Gather(
            input="speech",
            action="/process-speech",
            method="POST",
            speech_timeout="auto",
            language="en-US"
        )
        gather.say("Sorry, I didn't catch that. Could you repeat?")
        response.append(gather)
        return Response(content=str(response), media_type="application/xml")
    
    # Get AI response
    ai_text = get_ai_response(user_speech)
    
    # Convert to ElevenLabs voice
    try:
        audio_bytes = text_to_speech(ai_text)
        
        # Save audio temporarily and serve it
        audio_b64 = base64.b64encode(audio_bytes).decode()
        
        # Store in memory for serving
        app.state.latest_audio = audio_bytes
        
        response = VoiceResponse()
        gather = Gather(
            input="speech",
            action="/process-speech",
            method="POST",
            speech_timeout="auto",
            language="en-US"
        )
        # Play ElevenLabs audio then listen
        gather.play(f"{os.environ.get('BASE_URL')}/audio")
        response.append(gather)
        
    except Exception as e:
        print(f"TTS error: {e}, falling back to basic voice")
        response = VoiceResponse()
        gather = Gather(
            input="speech",
            action="/process-speech",
            method="POST",
            speech_timeout="auto",
            language="en-US"
        )
        gather.say(ai_text)
        response.append(gather)
    
    return Response(content=str(response), media_type="application/xml")

@app.get("/audio")
async def serve_audio():
    from fastapi.responses import Response as FastAPIResponse
    audio = getattr(app.state, 'latest_audio', None)
    if audio:
        return FastAPIResponse(content=audio, media_type="audio/mpeg")
    return FastAPIResponse(content=b"", media_type="audio/mpeg")

@app.get("/health")
async def health():
    return {"status": "running"}