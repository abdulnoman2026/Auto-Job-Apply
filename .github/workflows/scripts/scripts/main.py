#!/usr/bin/env python3
import os
import requests
from datetime import datetime

# Get environment variables
adzuna_key = os.environ.get('ADZUNA_API_KEY')
gmail_pass = os.environ.get('GMAIL_PASSWORD')
whatsapp = os.environ.get('WHATSAPP_NUMBER')

print(f"[{datetime.now()}] Job automation started!")
print(f"API Key: {'✓' if adzuna_key else '✗'}")
print(f"Gmail Password: {'✓' if gmail_pass else '✗'}")
print(f"WhatsApp Number: {'✓' if whatsapp else '✗'}")

print("Job search completed!")
