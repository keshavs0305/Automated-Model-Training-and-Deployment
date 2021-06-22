import json
import boto3
import datetime

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    
    status_code = client.start_execution(
        stateMachineArn='arn:aws:states:ap-south-1:996973542545:stateMachine:mlops-train-and-deploy',
        name= str(datetime.datetime.now().timestamp())[:10]
        )
    return