from flask import Flask, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config.Config')
mail = Mail(app)

@app.route("/send/", methods=["POST"])
def send_email():
    data = request.get_json()
    recipient_email = data["recipient_email"]
    text = data["text"]
    html_text = "<b>{0}</b>".format(text)
    msg = Message("Momentum Valasztasi Portal Kerdes", sender="cswart@outlook.com", recipients=[recipient_email], html = html_text.format(text),)
    print(msg)
    mail.send(msg)
    return jsonify(sender="cswart@outlook.com", recipients=[recipient_email], html = html_text, success=True)


