import re

def validate_contact(record):
    try:
        company_id = int(record['user_id'])
    except ValueError:
        return False, "Invalid Company_id (must be an integer)"
    
    email = record['email']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Invalid email format"

    phone = record['phone']
    phone_regex = r'^\d{3}-\d{3}-\d{4}$'
    if not re.match(phone_regex, phone):
        return False, "Invalid phone number format (expected xxx-xxx-xxxx)"
    
    zip_code = record['zip']
    if not zip_code.isdigit() or len(zip_code) != 5:
        return False, "Invalid zip code (must be 5 digits)"
    
    return True, "Valid data"




