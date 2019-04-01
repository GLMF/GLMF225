from PyInquirer import prompt

widget = [
    {
        'type': 'expand',
        'name': 'serie',
        'message': 'Quelle est votre série préférée ?',
        'choices': [
            {
                'key': 'g',
                'name': 'Game of Thrones',
                'value': 'GoT'
            },
            {
                'key': 'l',
                'name': 'Lucifer',
                'value': 'lucifer'
            },
            {
                'key': 'w',
                'name': 'Westworld',
                'value': 'westworld'
            }
        ]
    }
]

result = prompt(widget)
