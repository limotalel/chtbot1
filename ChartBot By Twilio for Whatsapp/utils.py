# Standard library import
import logging

# Third-party imports
from twilio.rest import Client
import decouple

# Find your Account SID and Auth Token at twilio.com
account_sid = "AC0889071abbe467be25e3005281b7a521"
auth_token = "9ca07ec985199fa4b217ef8cb3065699"
client = Client(account_sid, auth_token)
twilio_number = "+14155238886"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sending message logic through Twilio Messaging API
def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=body_text,
            to=f"whatsapp:{to_number}"
            )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")