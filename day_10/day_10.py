def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calc(prev_res=None):
    operation = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    if prev_res is None:
        num1 = int(input('first number'))
    else:
        num1 = prev_res
    num2 = int(input('second number'))

    for symbol in operation:
        print(symbol)
    operation_symbol = input('choose a symbol')
    calculation_function = operation[operation_symbol]
    result = calculation_function(num1, num2)
    print(result)
    again = input('another one?')
    if again == 'y':
        calc(prev_res=result)
    else:
        return result


calc()