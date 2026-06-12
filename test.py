from lambda_function import lambda_handler

event = {
    "name": "Sabitha"
}

output = lambda_handler(event, None)

print(output)