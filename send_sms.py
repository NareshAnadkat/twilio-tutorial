from twilio.rest import TwilioRestClient


message = client.messages.create(body="Hello from Python",
    to="+16474541614",    # Replace with your phone number
    from_="+16473603234") # Replace with your Twilio number

print(message.sid)
