import os
import resend
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_oauth import get_google_credentials

resend.api_key = "you_resend_key"

def send_email(to_email, subject, content):
    try:
        email = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [to_email],
            "subject": subject,
            "text": content
        })
        return email
    except Exception as e:
        print(f"[Resend] 发送邮件出错: {e}")
        return None

def send_email_google(to_email, subject, content):
    try:
        print("[DEBUG] 正在尝试通过 Gmail 发送邮件...")
        creds = get_google_credentials()
        service = build("gmail", "v1", credentials=creds)

        message = MIMEText(content)
        message["to"] = to_email
        message["subject"] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        body = {"raw": raw}

        message = service.users().messages().send(userId="me", body=body).execute()
        return message
    except Exception as e:
        print(f"[Google] 发送邮件出错: {e}")
        return None
