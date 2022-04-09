import json

texto = '''{
    'error': {
        'code': 400,
        'message': "INCORRECT_PASSWORD",
        'errors': [
            {
                'message': 'INCORRECT_PASSWORD',
                'domain': 'global',
                'reason': 'incorrect'
            }
        ]
    }

}'''

formato = json.loads(texto)

error = formato['error']
print = (error['message'])