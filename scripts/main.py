#!/usr/bin/env python3
import os
import smtplib
from email.mime.text import MIMEText

adzuna_key = os.environ.get('ADZUNA_API_KEY')
gmail_pass = os.environ.get('GMAIL_PASSWORD')
whatsapp = os.environ.get('WHATSAPP_NUMBER')

print("Job automation started!")
print(f"API Key: {'OK' if adzuna_key else 'MISSING'}")
print(f"Gmail: {'OK' if gmail_pass else 'MISSING'}")
print(f"WhatsApp: {'OK' if whatsapp else 'MISSING'}")

# Send email
try:
    msg = MIMEText("Your job automation is running! 🎉")
    msg['Subject'] = "Job Automation Running"
    msg['From'] = "abdulnoman2026@gmail.com"
    msg['To'] = "abdulnoman2026@gmail.com"
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("abdulnoman2026@gmail.com", gmail_pass)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent!")
except Exception as e:
    print(f"❌ Email failed: {e}")

print("Job search completed!")
