import csv
import os
filename =""
def get_filename_and_tableName():
    filename = input("Enter the CSV file name (with extension): ")
    tableName = os.path.splitext(filename)[0]
    return filename, tableName

def read_and_store_csv(name):
    filename = name
    
    data_list = []  
    
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                data_list.append(row)
            return data_list 

    except FileNotFoundError:
        print(f"The file '{filename}' was not found. Please check the filename and try again.")

