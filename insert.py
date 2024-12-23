import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
from read_csv import get_filename_and_tableName

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')
try:
        dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
        )  
except (NoCredentialsError, PartialCredentialsError) as e:
    print("Error: AWS credentials not found or incomplete.")
    print(f"Details: {e}")

def get_dynamodb_table(name, primary_key):    
    try:
        table_Name = name
        table = dynamodb.Table(table_Name) 
        table.load() 
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            key_schema = [
                {
                    'AttributeName': primary_key,
                    'KeyType': 'HASH'  
                }
            ]

            attribute_definitions = [
                {
                    'AttributeName': primary_key,
                    'AttributeType': 'N'  
                }
            ]

            provisioned_throughput = {
                'ReadCapacityUnits': 100,
                'WriteCapacityUnits': 100
            }

            try:
                response = dynamodb.create_table(
                    TableName=table_Name,
                    KeySchema=key_schema,
                    AttributeDefinitions=attribute_definitions,
                    ProvisionedThroughput=provisioned_throughput
                )
                print(f"Table: '{table_Name}' created successfully!")
                print(response)
            except Exception as e:
                print(f"Error creating table: {e}")
    return table 

def insert_into_dynamodb(record, filename):
    columns = record.keys()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",record)
    primary_key = next(iter(record))
    table = get_dynamodb_table(filename,primary_key)
    # try:
    response = table.put_item(
        Item=record
    )
    # except Exception as e:
    #     print(f"Error inserting record: {e}")
  