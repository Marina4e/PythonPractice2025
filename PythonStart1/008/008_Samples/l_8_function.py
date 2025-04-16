# def print_sum():
#     print(2+2)
#
#
# # what could be inside body of the function
# def example_1():
#     """
#     Here is docstring describe what is going on inside function
#     """
# print(example_1())  # -> None
#
# def example_2():
#     pass  # оператор заглушка
# print(example_2())  # -> None
#
# def example_2():
#     ...  # оператор заглушка
# print(example_2())  # -> None
#
# # arguments
# def sum_two_numbers(a, b):
#     return a + b
#
#
# print(sum_two_numbers(12, 2))
#
# result = sum_two_numbers(10, 1)
# print(result)
#
# # позиційні аргументи
# def printing_positional_args(first, second):
#     print(second, first, 'зміна позицій аргументів змінює порядок')
#     print(first, second)
#
#
# # if you have more then 2 atr
# def sum_two_numbers(a, b, *args):
#     return a + b + sum(args)
#
# # v2
# def user_greetings(name, surname, *additional_information):
#     return f"hello {name} {surname}\n your information is {additional_information}"  # але краще args
#
# # ключові аргументи
#
# def printing_positional_args(first, second):
#     print(f'{first=}, {second=}')
#
#
# printing_positional_args(first='First', second='Second')
#
# def example_keyword(first=None, second='Second'):
#     return first, second
#
# print(example_keyword())
#
# # можна комбінувати але позіційні перші
# def example_keyword(first, second=None, third='Second'):
#     return first, second, third
#
# print(example_keyword('1'))
#
# # а чи можна передати ключових більше ніж потрібно?
# def example_keyword(first, second=None, third='Second', **kwargs):
#     return first, second, third, kwargs
#
# print(example_keyword('1'))

# def make_pizza(*toppings):
#     for topping in toppings:
#         print(f" - {topping}")
#
#
# make_pizza('mushrooms', 'sausages', 'cheese', 'capers')
#
#
numbers_l = [1, 2, 3]
def reversing_list_numbers(numbers: list):
    # l = listic.copy()
    numbers.reverse()
reversing_list_numbers(numbers_l)
print(numbers_l)

# """Знайдіть максимальне значення в списку, що передається в функцію, і поверніть його,
#  якщо воно більше 0, в іншому випадку поверніть повідомлення про те, що число менше 0."""
#
# def finding_max_value_in_list(max_list: list):
#     result = 0
#     for e in max_list:
#         if e > result:
#             result = e
#     if result == 0:
#         return 'number less then zero or equal '
#     else:
#         return result
# print(finding_max_value_in_list([-1,-2,-3,-4]))
# # v2
# def finding_max_value_in_list_2(max_list: list):
#     result = 0
#     for e in max_list:
#         if e > result:
#             result = e
#
#     return 'number less then zero or equal ' if result == 0 else result
#
# print(finding_max_value_in_list_2([-1,-2,-3,4]))
#
# # v3
# def finding_max_value_in_list_3(max_list: list):
#     result = max(max_list)
#     return 'number less then zero or equal ' if result <= 0 else result
#
# print(finding_max_value_in_list_3([-1,-2,-3,-4]))
#
# """Поверніть кількість літер у слові, яке надсилається у параметрах."""
# # v1
# def counting_letters_word(word: str):
#     return len(word)
# print(counting_letters_word('hello'))
#
# """Напишіть функцію, яка зводить до ступеня число, яке передається у параметрах,
#  якщо ступінь не є негативним.
#  Перший параметр - число, другий – ступінь, у якому його необхідно звести."""
# def exponentiate_number(number, power):
#     if power > 0:
#         return pow(number, power)
#     else:
#         return power
#
# print(exponentiate_number(2, 2))

