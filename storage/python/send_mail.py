# send_mail.py

import sys
import os
import json
from aws_mailer import AwsMailer

if len(sys.argv) < 5:
    print("Usage: send_mail.py <to_email> <subject> <body_html> <sender_email>")
    sys.exit(1)

to_email = sys.argv[1]
subject = sys.argv[2]
body_html = sys.argv[3]
sender_email = sys.argv[4]

mailer = AwsMailer(
    aws_region="us-west-2",
    aws_access_key=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    sender_email=sender_email
)

response = mailer.send_email(
    recipient_email=to_email,
    subject=subject,
    body_html=body_html
)

if response and 'MessageId' in response:
    print(json.dumps({
        "status": "success",
        "message_id": response['MessageId']
    }))
else:
    print(json.dumps({
        "status": "error",
        "message": "Failed to send email"
    }))
