import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://famine-dig-dealmaker.ngrok-free.dev/incoming-call",
   to="+923184057200",  # Your real Pakistani number here
    from_=os.environ["TWILIO_PHONE_NUMBER"],
)

print(f"📞 Calling you now! Call SID: {call.sid}")