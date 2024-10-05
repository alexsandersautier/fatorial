def validate(number): 
    if not str(number).isnumeric() and not isinstance(number, int):
        return "Para que se possa realizar o calculo da fatorial o valor digitado precisa ser um número inteiro maior ou igual a zero"

    number = int(number)

    if number < 0:
        return "Para que se possa realizar o calculo da fatorial o valor digitado precisa ser um número inteiro maior ou igual a zero"

    return number

def calculate_fatorial(number, toValidate):
    if toValidate:
        result = validate(number)
        if not result ==int(number):
            return result
    number = int(number)
    if number <= 1:
        return 1
    else:
        return number * calculate_fatorial(number - 1, False)
    