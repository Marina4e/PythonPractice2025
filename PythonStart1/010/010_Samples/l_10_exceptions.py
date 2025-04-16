# Винятки
print('first step')
1/0
print('second step')

def sum(first_arg, second_arg):
    return first_arg - second_arg

print(sum('asdf', 1))



def divide_two_numbers(first, second):
    try:
        answer = first / second
    except ZeroDivisionError:
        return "you couldn't divide on zero"
    except (TypeError, Exception):
        return "you couldn't divide different types of object"
    else:
        print('else if in try anything is OK')
    finally:
        return 'FINALLY'



    return answer

print(divide_two_numbers(1, 0))

print('The code go further')

def bool_return():
    try:

        return True
    finally:
        return False

print(bool_return())
try:
    raise ZeroDivisionError
except:
    print('I catch raised error')

if 1 != 2 :
    raise AssertionError

assert 1==2

import math
from math import minus

raise ImportError

assert 'False' == 'Falsee'


# Практичні задачі
# Task 1
"""Реалізувати функцію, яка прийматиме на вхід номер місяця, 
повернути його назву та реалізувати в ньому кілька обробок винятків.
"""


def month_name(month_number):
    months = ['January', 'February', 'March',
              'April', 'May', 'Jun', 'July',
              'August', 'September', 'October',
              'November', 'December']
    try:
        month_index = abs(month_number) - 1
        return months[month_index]
    except TypeError:
        return 'Please use only integers'
    except IndexError:
        return 'Please use integers between 1 and 12'


print(month_name(12))

assert month_name(12) == 'December'

# Task 2
"""Потрібно перевірити, чи всі числа в послідовності
 є унікальними і реалізувати кілька обробок винятків"""

def is_sequence_unique(sequence):
    try:
        return len(sequence[:]) == len(set(sequence))
    except TypeError as e:
        return f'Type error need to use only sequence type(str, list, range, tuple) \n Error: {e}'


print(is_sequence_unique({'key':'value'}))


class TurnOffLightError(Exception):
    def __str__(self):
        return 'You forgot to turn off the light'



try:
    raise TurnOffLightError
except TurnOffLightError as e:
    print(f'Erorr message: {e}')
