# model.py

import re

def validate_username(username):
    """Validate username: must be alphanumeric and 6-15 characters long."""
    if 6 <= len(username) <= 15 and username.isalnum():
        return True
    return False

def validate_password(password):
    """Validate password: must contain at least one number, one uppercase letter, 
    one lowercase letter, and be at least 8 characters long."""
    if (len(password) >= 8 and
        re.search(r'[0-9]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password)):
        return True
    return False
