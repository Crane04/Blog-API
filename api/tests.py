

from termii_sdk import TermiiSDK
from termii_sdk.core import Request

# Default sdk termii_enpoint
# TERMII_ENDPOINT = "https://api.ng.termii.com/api"

Request.termii_endpoint = 'https://api.ng.termii.com/api'

# Initialize the SDK with your API key
api_key = "TLHKTx4PgWm9Ebm2EOb9aQ4h8UNv0qjOZHHquaKaLmBBag1ihNOGWq8QcgQ9bJ"
termii = TermiiSDK(api_key)
rq = 0

# Send an SMS message
message = "Hello from Termii SDK!"
phone_number = "+2349114081137"
from_ = "Mayowa"
response = termii.send_message(from_ = from_,to=phone_number, sms=message)
print("Message ID:", response.get("message_id"))