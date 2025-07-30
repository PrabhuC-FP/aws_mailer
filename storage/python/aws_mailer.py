# aws_mailer.py

import boto3
from botocore.exceptions import ClientError

class AwsMailer:
    def __init__(self, aws_region, aws_access_key, aws_secret_key, sender_email):
        self.sender = sender_email
        self.ses = boto3.client(
            'ses',
            region_name=aws_region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def send_email(self, recipient_email, subject, body_html, body_text=None):
        if body_text is None:
            body_text = "This email requires an HTML-compatible viewer."

        try:
            response = self.ses.send_email(
                Source=self.sender,
                Destination={
                    'ToAddresses': [recipient_email],
                },
                Message={
                    'Subject': {'Data': subject},
                    'Body': {
                        'Text': {'Data': body_text},
                        'Html': {'Data': body_html}
                    }
                }
            )
            return response
        except ClientError as e:
            print("Error:", e.response['Error']['Message'])
            return None
