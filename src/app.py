import json


def who(who):
    return {
        "statusCode": 200,
        "body": f"Hello {who}\n",
    }


def get_hello(event, context):
    return who(event["queryStringParameters"]["who"])


def post_hello(event, context):
    payload = json.loads(event["body"])
    return who(payload["who"])


def lambda_handler(event, context):
    # print(event)

    # GETとPOST両用ハンドラ
    if event["httpMethod"] == "GET":
        return get_hello(event, context)
    elif event["httpMethod"] == "POST":
        return post_hello(event, context)

    return who("Unsupported Method")
