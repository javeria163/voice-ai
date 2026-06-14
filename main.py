import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("🚀 Starting Voice AI Server...")
    print("📞 Waiting for calls...")
    print("🌐 Server running on http://localhost:8000")
    print("❤️  Health check: http://localhost:8000/health")
    
    uvicorn.run(
        "call_handler:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )