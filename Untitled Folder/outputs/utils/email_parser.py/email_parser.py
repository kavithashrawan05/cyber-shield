# email_parser.py

import re

def detect_phishing(subject, body):
    """
    Detects phishing based on suspicious keywords in subject and body.
    Returns True if phishing is suspected, else False.
    """
    suspicious_keywords = [
        'verify', 'reset', 'urgent', 'click here', 'login now',
        'account suspended', 'update info', 'confirm identity',
        'security alert', 'limited time', 'password expired'
    ]
    
    combined_text = (subject + " " + body).lower()
    
    for keyword in suspicious_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', combined_text):
            return True
    return False