import phonenumbers
from phonenumbers import NumberParseException

import re

def clean_phone_number(raw_number=None) -> str:
    if not raw_number or not str(raw_number).strip():
        return "INVALID"

    digits = re.sub(r"\D", "", str(raw_number))

    if len(digits) == 10:
        return "+1" + digits
    elif len(digits) == 11 and digits.startswith("1"):
        return "+" + digits

    return "INVALID"
    
    
def extract_area_code(phone):
    """
    Extracts the area code (3-digit code) from a phone number.

    Supported formats:
        +1-415-555-1234
        415-555-1234
        (415) 555-1234
        4155551234

    Parameters:
        phone (str): Raw phone number string

    Returns:
        str: 3-digit area code if found, otherwise None
    """

    if phone is None:
        return None

    # Convert to string in case numeric input comes in
    phone = str(phone)

    # Remove all non-numeric characters except +
    cleaned = re.sub(r"[^\d+]", "", phone)

    # Remove country code if present (e.g., +1)
    if cleaned.startswith("+1"):
        cleaned = cleaned[2:]

    # Now extract first 3 digits as area code
    match = re.match(r"(\d{3})", cleaned)

    if match:
        return match.group(1)

    return None
    
    
    
def mask_phone_number(phone):
    """
    Convert:
    +14155551234 -> XXX-XXX-1234
    4155551234   -> XXX-XXX-1234
    """

    if phone is None:
        return None

    digits = re.sub(r"\D", "", str(phone))

    if len(digits) < 4:
        return "INVALID"

    return f"XXX-XXX-{digits[-4:]}"
