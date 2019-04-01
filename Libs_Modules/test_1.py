from PyInquirer import prompt, Validator, ValidationError, style_from_dict, Token
from prompt_toolkit import document
import regex

style = style_from_dict(
    {
        Token.Separator: '#E3AF3F',
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#800000',
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',
        Token.Answer: '#2196f3 italic',
        Token.Question: ''
    }
)

class DateValidator(Validator):
    def validate(self, document : document.Document) -> None:
        ok = regex.match('^(([0-2][0-9])|(3[0-1]))/((0[0-9])|(1[0-2]))/\d{4}$', document.text)
        if not ok:
            raise ValidationError(
                message = 'Veuillez saisir une date valide (format jj/mm/aaaa)',
                cursor_position = len(document.text))

widget = [
    {
        'type': 'input',
        'name': 'date',
        'message': 'Saisissez une date au format jj/mm/aaaa :',
        'validate': DateValidator
    }
]

result = prompt(widget, style=style)
print(f'Date saisie : {result["date"]}')
