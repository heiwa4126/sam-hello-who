import json


def lambda_handler(event, context):
    print(event)
    who = event["queryStringParameters"]["who"]
    return {
        "statusCode": 200,
        "body": f"Hello {who}\n",
    }
