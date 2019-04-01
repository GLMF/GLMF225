from PyInquirer import prompt
from typing import Dict, Any

def checkDisplay(answers : Dict[str, Any]) -> bool:
    return answers['autre']

widget = [
    {
        'type': 'confirm',
        'name': 'autre',
        'qmark': '>',
        'message': 'Une autre question ?',
        'default': True
    },
    {
        'type': 'password',
        'name': 'password',
        'qmark': '>',
        'message': 'Mot de passe :',
        'when': lambda answers : checkDisplay(answers)
    }
]

result = prompt(widget)
