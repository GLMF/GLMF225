from PyInquirer import prompt

widget = [
    {
        'type': 'list',
        'name': 'series',
        'message': 'Série préférée (sélection dans la liste) :',
        'choices': ['Game of Thrones', 'Lucifer', 'Elementary', 'Friends', 'Westworld']
    }
]

result = prompt(widget)
