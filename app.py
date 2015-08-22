import os
from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond_with_tone():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()
    resp.say("Only grills are allowed in the secret lair. First you must prove you are worthy.")
    # gather 4 digits
    with resp.gather(numDigits=4, action="/handle-passphrase", method="POST") as prompt:
        prompt.say("Please enter the secret password to enter Shane and Jerome's secret lair.")
# temporary
#    tone = "9"
#    resp.play(digits=tone)

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
        bad_resp.say("You're obviously not cool enough to join the secret lair. Come back when you are 20% cooler.")
        return str(bad_resp)
 
if __name__ == "__main__":
    #SECRET_PHRASE = "1337" # THE SECRET

    import logging
    #logging.basicConfig(filename='error.log',level=logging.DEBUG)
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('error.log')
    logger.addHandler(handler)
    app.logger.addHandler(handler)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
