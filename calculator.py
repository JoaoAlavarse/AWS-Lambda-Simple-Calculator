import json

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    
    oneValue = body.get('oneValue')
    anotherValue = body.get('anotherValue')
    operation = body.get('operation')
    response = 0
    
    if oneValue is None:
        raise Exception('oneValue não pode ser vazio ou nulo')
        
    if anotherValue is None:
        raise Exception('anotherValue não pode ser vazio ou nulo')
        
    if operation is None:
        raise Exception('operation não pode ser vazio ou nulo')
        
    if not isinstance(oneValue, (int, float)):
        raise Exception('oneValue precisa ser numérico')
        
    if not isinstance(anotherValue, (int, float)):
        raise Exception('anotherValue precisa ser numérico')
        
    if not isinstance(operation, (str)):
        raise Exception('operation precisa ser um texto')
        
    if operation != 'plus' and operation != 'minus' and operation != 'times' and operation != 'divided':
        raise Exception('operation precisa ser: minus, plus, times ou divided')
        
    if operation == 'plus':
        response = oneValue + anotherValue
        
    if operation == 'minus':
        response = oneValue - anotherValue
        
    if operation == 'times':
        response = oneValue * anotherValue
        
    if operation == 'divided':
        if anotherValue == 0:
            raise Exception('anotherValue não pode ser zero')
        response = oneValue / anotherValue
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
