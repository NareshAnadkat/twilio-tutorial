from flask import Flask, request, redirect, session
from twilio import twiml
import requests
import json

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+16474541614": "Naresh",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with the number of text messages sent between two parties."""

    counter = session.get('counter', 0)

    # increment the counter
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Monkey"

    ticker = request.values.get("Body")

    resp = twiml.Response()

    response = requests.get("http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol=" + ticker)

    raw_json = response.text.split("(")[3].strip(")")  # convert to json
    parsed_json = json.loads(raw_json)

    if "LastPrice" in parsed_json:
        last_price = parsed_json["LastPrice"]
        resp.sms("The last price of " + ticker + " is " + str(last_price))
    else:
        resp.sms("Hi there! Thanks for using Naresh's Stock bot. To start off, please enter a valid ticker symbol you would like to know the current price of.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
