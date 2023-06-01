from twilio.rest import Client
# from vis.visual import activity_dict


# Your Twilio account SID and auth token
account_sid = 'AC551960cde1bdda9b9f76fbe1336d1105'
auth_token = '3c873404c5dcb6fc39921636320d24c9'

# Create a Twilio client object
client = Client(account_sid, auth_token)

# Define the message content
  # Replace activity_id with the ID of the activity that triggered the fall
message_body = f'Attention! A person has fallen. Please check on them immediately.'

# # Make a call
# call = client.calls.create(
#     to='+916369251768',  # Replace with the phone number you want to call
#     from_='+916369251768',  # Replace with your Twilio phone number
#     url='http://demo.twilio.com/docs/voice.xml',  # Replace with the URL of your TwiML voice script
#     twiml=f'<Response><Say>{message_body}</Say></Response>'
# )

# Send a message
message = client.messages.create(
    to='+916369251768',  # Replace with the phone number you want to message
    from_='+12707169134',  # Replace with your Twilio phone number
    body=message_body
)

messagewp = client.messages.create(
    from_='whatsapp:+14155238886', # Replace with your Twilio WhatsApp phone number
    to='whatsapp:+916369251768',  # Replace with the recipient's WhatsApp phone number
    body=message_body
)