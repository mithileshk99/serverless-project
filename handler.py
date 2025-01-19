import json

def hello(event, context):
    body = {
        "message": "Hello AWS - Zero To Hero Batch"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def bye(event, context):
    body = {
        "message": "3...2...1... Bye"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                                                                                          
~                        
