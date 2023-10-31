import os
import csv
import boto3

# Initialize the AWS clients for S3 and DynamoDB
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Set the name of your S3 bucket and DynamoDB table
S3_BUCKET_NAME = 'your-s3-bucket-name'
DYNAMODB_TABLE_NAME = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    # Iterate through all the records in the event
    for record in event['Records']:
        # Get the S3 bucket and object key from the record
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Read the CSV file from S3
        s3_object = s3.get_object(Bucket=bucket, Key=key)
        csv_data = s3_object['Body'].read().decode('utf-8').splitlines()

        # Initialize the DynamoDB table
        table = dynamodb.Table(DYNAMODB_TABLE_NAME)

        # Process the CSV data and save it to DynamoDB
        for row in csv.reader(csv_data):
            # Assuming the first column is the primary key
            primary_key = row[0]
            # Create a dictionary for item insertion
            item = { 
                'PrimaryKeyColumn': primary_key,
                'OtherColumn1': row[1],
                'OtherColumn2': row[2],
                # Add more columns as needed
            }

            # Save the item to DynamoDB
            table.put_item(Item=item)

        print(f"Data from {key} saved to DynamoDB")

# The Lambda function will be triggered by S3 events, so you should configure the S3 bucket to send events to this Lambda function.
