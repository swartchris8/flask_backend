## Install

Recommended to activate a virtualenv and then run:

pip install -r requirements.txt

Fill in config.py with the email details you want to use, DONT COMMIT YOUR ACCOUNT AND PASSWORD!

Run the app with

gunicorn app:app

And use the example curl request to send emails see curl.example