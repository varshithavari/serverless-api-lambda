from lambda_function import lambda_handler

event = {
    "name": "Varshitha"
}

output = lambda_handler(event, None)

print(output)
