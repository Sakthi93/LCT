# main

# Import the read_and_store_csv function from the file_reader module
# main.py
from read_csv import read_and_store_csv , get_filename_and_tableName 
from contact_validation import validate_contact
from company_validation import validate_company
from insert import insert_into_dynamodb

def main():
    filename = get_filename_and_tableName()
    records  = read_and_store_csv(filename[0])
    
    if records  and filename[1] == "contact":
        for record in records:
                is_valid, message = validate_contact(record)
                if is_valid:                    
                    insert_into_dynamodb(record,filename[1])
                else:
                    pass
                    
    elif filename[1] == "company":
        for record in records:
           is_valid, message = validate_company(record)
           if is_valid:                    
                    insert_into_dynamodb(record,filename[1])
           else:
               pass
    
           
      

if __name__ == "__main__":  
    main()