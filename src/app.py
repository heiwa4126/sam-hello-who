import json


def get_hello(event, context):
    who = event["queryStringParameters"]["who"]
    return {
        "statusCode": 200,
        "body": f"Hello {who}\n",
    }


def post_hello(event, context):
    payload = json.loads(event["body"])
    return {
        "statusCode": 200,
        "body": f"Hello {payload['who']}\n",
    }


def lambda_handler(event, context):
    print(event)
    if event["httpMethod"] == "GET":
        return get_hello(event, context)
    elif event["httpMethod"] == "POST":
        return post_hello(event, context)

    return {
        "statusCode": 200,
        "body": "Something fishy...\n",
    }
