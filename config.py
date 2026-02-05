import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

TO_NUMBER = os.environ["TO_NUMBER"]
FROM_NUMBER = os.environ["FROM_NUMBER"]

api_key = os.environ["OWM_API_KEY"]

