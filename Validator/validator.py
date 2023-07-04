stroka = input('Введите строку\n')

def validator(string: str):
    return string.count('[') == string.count(']') and string.count('(') == string.count(')') and string.count('{') == string.count('}')


print(validator(stroka))