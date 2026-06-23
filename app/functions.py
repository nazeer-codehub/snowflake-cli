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
