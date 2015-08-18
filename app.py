import os
from flask import Flask
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def respond_with_tone():
    """Respond to incoming requests."""
    tone = "9" # the tone keypress you would like to send

    resp = twilio.twiml.Response()
    resp.play(digits=tone)
 
    return str(resp)
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
