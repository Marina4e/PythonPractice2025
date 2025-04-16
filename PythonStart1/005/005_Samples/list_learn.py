# Знайти та видалити всі парні елементи списку.
# list_of_numbers = [2, 4, 1, 7, 3, 55, 98, 2, 12]
# copy_list_of_numbers = list_of_numbers.copy()
# index = 0
# while True:
#     if index < len(list_of_numbers):
#         if list_of_numbers[index] % 2 == 0:
#             copy_list_of_numbers.remove(list_of_numbers[index])
#         index += 1
#     else:
#         break
#
# print(copy_list_of_numbers)

#
# list_of_numbers = [2, 4, 1, 7, 3, 55, 98, 2, 12]
# copy_list_of_numbers = list_of_numbers.copy()
# for num in list_of_numbers:
#     if num % 2 == 0:
#         copy_list_of_numbers.remove(num)
#
#
# print(copy_list_of_numbers)

# Звести всі елементи списку в квадрат.
# list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# list_numbers_squares = list()  # []
#
# for num in list_numbers:
#     list_numbers_squares.append(num**2)
#
# print(list_numbers_squares)
# print('~~' * 16)
#
# for index in range(len(list_numbers)):
#     list_numbers[index] = list_numbers[index] ** 2
#
# print(list_numbers)


# Знайти максимальний елемент списку.

# variant 1
element_any = [4, 2, 1, 5, 7, 4, 3, 1]

maximum = element_any[0]
for e in range(1,len(element_any)):
    if element_any[e] > maximum:
        maximum = element_any[e]

# print(maximum)
# v2
# print(max([4, 2, 1, 5, 7, 4, 3, 1]))

# V3
# print(sorted(element_any)[-1])

# V4
element_any.sort()
print(element_any[-1])

