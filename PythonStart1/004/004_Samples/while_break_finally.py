'''
    конструкція while   призначена для організації циклів з невідомою кількістю повторень
    while умова bool:
        інструкція1
        інструкція2
    інструкція за циклом.
'''

# counter = 50
# while counter > 0:
#     counter -= 1
#     print(f'залишилось посадити {counter}')
#
# print('за лічильником')
# print(f'Все досить саджати. {counter}')

# range(6)
# [0, 1, 2, 3, 4, 5]
# for i in range(11):
#     print(f'Hello python developer {i}')

# counter = 10
# while True:
#     # counter = counter - 1
#     counter -= 1
#     print(counter)
#     if counter == 5:
#         break
#         print('Чи буде друкуватись текст після break???')
#
# print('Далі після While...')

# counter = 0
# while counter < 10:
#     counter += 1
#     if (counter % 2) == 0:
#         continue
#     print(counter)

# for e in range(4):
#     if e == 3:
#         break
#     print(e)

# for i in range(6):  # [0,1,2,3,4,5]
#     if i == 3:
#         continue
#     print(i)

# Пройтись діапазоном чисел від 0 до 101 і вивести в консоль тільки парні.
# for element in range(102):
#     if element != 0 and element % 2 == 0:
#         print(element)


# Пройтись за словом 'hello' та замінити всі літери l на літеру s.
# 'hello'
# for word in 'hello':
#     print(word)
# answer = ''
# for letter in 'hello':
#     if letter == 'l':
#         answer = answer + 's'
#     else:
#         answer = answer + letter
# print(answer)

# answer = ''
# for letter in 'hello':
#     if letter == 'l':
#         answer += 's'
#     else:
#         answer += letter
# # print(answer)
#
#
# print('hello'.replace('l', 's'))


# Вивести перше число з кінця, яке ділиться націло на 5. Діапазон від 99 до 0.

for e in reversed(range(100)):
    if e % 5 == 0:
        print(e)
        break

for i in range(-99, 0):
    if i % 5 == 0:
        print(abs(i))
        break

