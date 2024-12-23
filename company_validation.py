import re
import json

def load_json():
    with open('company_config.json', 'r') as json_file:
        return json.load(json_file)
valid_codes = load_json() 

def validate_company(record):
    if  record['company_code'] not in valid_codes['company_code']:
        return False, "Invalid company code"
    
    if  record['region_code'] not in valid_codes['region_code']:
        return False, "Invalid region code"
    
    duplicate_company_ids = []
    seen_company_ids = set()
    
    if int(record['Company_id']) not in seen_company_ids:
            seen_company_ids.add(record['Company_id'])
            
    else:
        duplicate_company_ids.add(record['Company_id'])
        
        if record['phone']:
            phone = record['phone']
            phone_regex = r'^\d{3}-\d{3}-\d{4}$'
            if not re.match(phone_regex, phone):
                return False, "Invalid phone number format (expected xxx-xxx-xxxx)"
        
        zip_code = record['zip']
        if not zip_code.isdigit() or len(zip_code) != 5:
            return False, "Invalid zip code (must be 5 digits)"
        
        if record['region_code']:
            region = record['region_code']
            region_regex = r"^[A-Za-z]{2}-\d{2}$"
            if not re.match(region_regex, region):
                return False, "Invalid phone number format (expected xxx-xxx-xxxx)"
            
    return True, "Valid data"