
import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = 'arn:aws:sns:ap-south-1:806525742801:file-upload'

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']

        message = f"New file uploaded!\nBucket: {bucket}\nFile: {file_name}"
        print(message)

        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject="S3 Upload Alert"
        )

        print("SNS Response:", response)

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }
