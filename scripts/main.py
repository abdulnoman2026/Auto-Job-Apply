#!/usr/bin/env python3
import os
from datetime import datetime

# Get secrets
adzuna_key = os.environ.get('ADZUNA_API_KEY')
gmail_pass = os.environ.get('GMAIL_PASSWORD')
whatsapp = os.environ.get('WHATSAPP_NUMBER')

print(f"[{datetime.now()}] Job automation started!")

# Test if all credentials are available
if adzuna_key and gmail_pass and whatsapp:
    print("✅ All credentials available!")
    print(f"✅ Will send email and WhatsApp notification")
    
    # Send test email
    try:
        import smtplib
        from email.mime.text import MIMEText
        
        msg = MIMEText("Job automation system is working!")
        msg['Subject'] = "Job Automation - Test Message"
        msg['From'] = "abdulnoman2026@gmail.com"
        msg['To'] = "abdulnoman2026@gmail.com"
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login("abdulnoman2026@gmail.com", gmail_pass)
            server.send_message(msg)
        print("✅ Email sent!")
    except Exception as e:
        print(f"❌ Email error: {e}")
    
    # Send WhatsApp message
    try:
        import requests
        url = f"https://api.callmebot.com/whatsapp.php"
        params = {
            "phone": whatsapp,
            "text": "Job automation system is running!",
            "apikey": "3542935"
        }
        requests.get(url, params=params)
        print("✅ WhatsApp message sent!")
    except Exception as e:
        print(f"❌ WhatsApp error: {e}")
else:
    print("❌ Missing credentials!")

print("Job automation completed!")
