def print_sum():
    print(2 + 2)


print_sum()


def example():
    pass  # заглушка


def example2():
    ...  # заглушка


def example3():
    """Docstring for information"""


print(help(example3))


def print_sum(a, b):
    print(a + b)


print_sum(1, 3)


def printing_positional_arguments(first, second, third, *anything_left):
    print(f"{first=}, {second=}", third, anything_left)


printing_positional_arguments('SECOND', 'FIRST', 'THIRD', 'fourth', 'fifth', '...', 23232, [], {})

first, second, third, *anything_left = ('FIRST', 'SECOND', 'THIRD', 'fourth', 'fifth', '...')
print(first, second, third, anything_left)


def print_sum(a, b, *elements):
    print(a + b + sum(elements))


print_sum(1, 3, 3, 2, 1, 3, 2, 1, 3, )


def make_pizza(*toppings):
    for topping in toppings:
        print(f"-{topping}")


make_pizza('muschrooms', 'sausages', 'cheese', 'capers')


# ключові аргументи

def printing_positional_arguments(first, second, third, *args):
    print(f"{first=}, {second=}", third)


# printing_positional_arguments(second='SECOND', first='FIRST', third='THIRD',)

def hello_user(job_position, name, surname, middlename='', **kwargs):
    print(kwargs)
    print(f"hello {name}  {surname} {middlename} your job position is {job_position} ")


hello_user('programmer', surname='Dil', name='Mark', work_country='Brazil', work_car='CAT')


def sum_two_numbers(a, b, *args):
    answer = [a + b + sum(args)]
    return answer


result = sum_two_numbers(3, 5, 4, 3, 2, 5, 23)
print(type(sum_two_numbers))

"""Знайдіть максимальне значення в списку, що передається в функцію, і поверніть його, якщо воно більше 0,
 в іншому випадку поверніть повідомлення про те, що число менше 0."""


def finding_max_value_in_list(numbers_list):
    max_value = 0
    for element in numbers_list:
        if element > max_value:
            max_value = element

    if max_value <= 0:
        return 'number less then zero or equal'
    else:
        return max_value


max_value_from_list = finding_max_value_in_list([-4, -5])
print(max_value_from_list)


# v2
def finding_max_value_in_list(numbers_list):
    max_value = max(numbers_list)
    return 'number less then zero or equal' if max_value <= 0 else max_value


max_value_from_list = finding_max_value_in_list([-4, -5, -9, -22])
print(max_value_from_list)

"""Поверніть кількість літер у слові, яке надсилається у параметрах."""


def counting_letters_word(word):
    return len(word)


number_letter = counting_letters_word('hello')
print(number_letter)

"""Напишіть функцію, яка зводить до ступеня число, яке передається у параметрах,
 якщо ступінь не є негативним. Перший параметр - число, другий – ступінь, у якому його необхідно звести."""


def exponentiate_number(number, power):
    if power > 0:
        return pow(number, power)
    return number


print(exponentiate_number(2, -2))

numbers = [1, 2, 3]


def reversing_list_numbers(n):
    n = n[:]
    n.reverse()
    return n


reversing_list_numbers(numbers)

print(numbers)
