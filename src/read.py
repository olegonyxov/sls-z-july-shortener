import os
import json
import boto3


dynamodb_client = boto3.client("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]

def handler(event, context):
    # get url_id from event
    url_id = event["pathParameters"]["url_id"]

    # get an item from URL_TABLE
    result = dynamodb_client.get_item(
        TableName=TABLE_NAME,
        Key={"url_id": {"S": url_id}}).get("Item")

    # result validation
    if not result:
        return {"statusCode": 404,
                "body":json.dumps({"error": "URL not found"})}

    #get long_utl from result
    long_url= result.get("long_url").get("S")

    #make redirect to long_url
    response = {
        "headers": {"Location": long_url},
        "statusCode": 301
    }
    return response