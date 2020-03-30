import boto3
import json

StepFuncARN="YOUR_STEP_FUN_ARN"

client = boto3.client('stepFunctions')

def lambda_handler(event, context):
    response = client.start_execution(
        stateMachineArn=StepFuncARN,
        input= json.dump(event)
    )

    print("Response: {}".format(response))
