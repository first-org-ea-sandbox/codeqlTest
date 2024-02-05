import json

def lambda_handler(event, context):
    # Print the input event for demonstration purposes
    print("Received event: " + json.dumps(event, indent=2))

    # Your actual logic goes here
    # ...

    # Return a response if needed
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
