import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ.get('HTTPS_PROXY')}

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token, http_client=proxy_client)

TO_NUMBER = os.environ["TO_NUMBER"]
FROM_NUMBER = os.environ["FROM_NUMBER"]

api_key = os.environ["OWM_API_KEY"]
