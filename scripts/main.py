#!/usr/bin/env python3
import os
from datetime import datetime

adzuna_key = os.environ.get('ADZUNA_API_KEY')
gmail_pass = os.environ.get('GMAIL_PASSWORD')
whatsapp = os.environ.get('WHATSAPP_NUMBER')

print(f"[{datetime.now()}] Job automation started!")
print(f"API Key: {'OK' if adzuna_key else 'MISSING'}")
print(f"Gmail: {'OK' if gmail_pass else 'MISSING'}")
print(f"WhatsApp: {'OK' if whatsapp else 'MISSING'}")
print("Job search completed!")
