import json

def lambda_handler(event, context):

    name = event.get("name", "User")

    response = {
        "statusCode": 200,
        "message": f"Hello, {name}! Welcome to AWS Lambda Simulation.",
        "service": "Serverless API",
        "success": True
    }

    return response