from twilio.rest import TwilioRestClient

account_sid = "AC877fd0e7f24d184704588e82f79a01de"
auth_token = "601d05c289207f015d901cff6f700770"
client = TwilioRestClient(account_sid, auth_token)


message = client.messages.create(body="Hello from Python",
    to="+16474541614",    # Replace with your phone number
    from_="+16473603234") # Replace with your Twilio number

print(message.sid)