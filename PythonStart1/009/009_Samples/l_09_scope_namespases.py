# global scope
# x = 2
# def print_x():
#     print(x)
#
# print_x()
# print(x)

# local scope
# y = 'global'
# def print_local_y():
#     y = 'local'
#     print(y)

# print_local_y()
#
# print(y)

"""
    Scope - область видимості
    Namespaces - простір імен. Існують для запобігання з пошуком імен
"""
# x = 1
# def print_namespace():  # імʼя фунції також записується у простір імен
#     """
#     Простір імен це словник з іменами та значеннями.
#     Разом з визначенням простору імен пайтон визначає і область видимості.
#     """
#     # print(1, locals())
#     date_founding_kiev = 482
#     # print(2, locals())
#     age = 2023 - 482
#     # print(3, locals())
#     print(globals())


# print_namespace()

# print(locals())

"""
Область видимості це ланцюжок просторів імен, який починається від локального і триває до глобального чи вбудованого.
Область видимості визначає те, в якому просторі імен Пайтон шукатиме визначення конкретного імені конкретної змінної та в якому
порядку цеї пошук буде здійснюватись. Для пошуку є аривіатура LEGB.  """




# def external():
#     'LEGB enclosed'
#     x = 1
#     def internal():
#         return x
#     return internal()
#
# print(external())



# internal()


# product = 'bread'  # Global variables
#
#
# def changing_product():
#     product = 'Milk'  # locals relates to changing_products and enclosed for showing_enclosed
#     print('Local: ', product)
#
#     def showing_enclosed():
#         # nonlocal product  # я буду змінювати вкладений простір імен
#         global product
#         print('Inside showing enclosed', product)
#         product = 'Cola'
#         print('Enclosed scope: ', product)
#
#     showing_enclosed()
#
#     print(product, '----')
#
#
# changing_product()
#
# print('Global:', product)

# lambda
# def foo(x):
#     return x
#
# l = lambda x: x


# print(l.__name__)
# print(foo.__name__)

# def power(x, y):
#     return x**y
#
# # print(power(2, 8))
#
# p = lambda x, y: x**y
# # print(p(2, 8))
#
# m = [4,3,2,5,6,4,3,1]
# m.sort(key=lambda x: -x)
# # print(m)
#
# def power3(x):
#     return x**3
#
# z = list(map(lambda x: x**3, m))
# print(z)


# Recursion
# print(globals(), '*'*10)
# def foo():
#     return foo()
#
# foo()
# print(globals())

# def foo(x: int) -> None:
#     if x < 10:
#         x += 1
#         foo(x)
#         print(x)
#
# # foo(1)
#
# def factorial(n: int)-> int:
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))
#
# print(1*2*3*4*5)



# Напишіть функцію, де дано натуральне число n. Виведіть усі числа від 1 до n.

def natural_int(n: int) -> None:
    if n >= 1:
        natural_int(n - 1)
        print(n)

# natural_int(12)

# Напишіть функцію для прорахунку площі прямокутника, у параметрах передаються висота та довжина.
def rectangle_are(height: int, lenght:int)-> int:
    return height*lenght
print(rectangle_are(2,2))

rectangle_are_l = lambda h, l: h*l
print(rectangle_are_l(3,3))


