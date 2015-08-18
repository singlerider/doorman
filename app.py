import os
from flask import Flask
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def respond_with_tone():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()
    # gather 4 digits
    with resp.gather(numDigits=4, action="/handle-passphrase", method="POST") as prompt:
        prompt.say("Please enter the secret password to enter Shane and Jerome's secret lair.")

    return str(resp)
    
@app.route("/handle-passphrase", method=['GET','POST'])
def handle_key():
    tone = "9" # the tone to open the door

    passphrase_entered = request.values.get('Digits', None)
    if passphrase_entered == SECRET_PHRASE:
        resp = twilio.twiml.Response()
        resp.play(digits=tone) # let them in!
 
    return str(resp)
 
if __name__ == "__main__":
    SECRET_PHRASE = "1337" # THE SECRET
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
