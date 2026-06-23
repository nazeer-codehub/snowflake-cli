from app.functions import clean_phone_number

def test_valid_us_number():
    assert clean_phone_number("(555) 123-4567") == "+15551234567"
    
def test_already_formatted():
    assert clean_phone_number("+15551234567") == "+15551234567"
    
def test_garbage_input():
    assert clean_phone_number("not a number") == "INVALID"
    
def test_empty_string():
    assert clean_phone_number() == "INVALID"