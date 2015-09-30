import os
from flask import Flask, request
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond_with_tone():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()
    resp.say("Why do you disturb my slumber. You must prove you are worthy to enter.")
    # gather 4 digits
    with resp.gather(numDigits=4, action="/handle-passphrase", method="POST") as prompt:
        prompt.say("Please enter the secret password to enter Shane and Jerome's secret lair.")

    return str(resp)
    
@app.route("/handle-passphrase", methods=['GET','POST'])
def handle_passphrase():
    tone = "9" # the tone to open the door
    SECRET_PHRASE = "1337"
    passphrase_entered = request.values.get('Digits', None)
    if passphrase_entered == SECRET_PHRASE:
        resp = twilio.twiml.Response()
        resp.play(digits=tone) # let them in!
        return str(resp)

    else:
        bad_resp = twilio.twiml.Response()
        bad_resp.say("Lame dude. You obviously don't know the password. Give up.")
        return str(bad_resp)
 
if __name__ == "__main__": # app gets run as app.py

    import logging # will help in the event of an unexpected error
    logger = logging.getLogger('werkzeug')
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
