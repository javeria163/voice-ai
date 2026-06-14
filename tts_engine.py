import os
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

def text_to_speech(text: str) -> bytes:
    print(f"🔊 Converting to speech: {text[:50]}...")
    
    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice - clear and natural
        text=text,
        model_id="eleven_turbo_v2",  # Fastest model for low latency
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.0,
            use_speaker_boost=True
        )
    )
    
    # Convert generator to bytes
    audio_bytes = b"".join(audio)
    print(f"✅ Audio generated: {len(audio_bytes)} bytes")
    return audio_bytes