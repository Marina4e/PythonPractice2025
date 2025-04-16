# a = 1
# b = 2
#
# if a > b:
#     result = a
# else:
#     result = b
#
# print(result)
# result = a if a > b else b
# books = 1
# if (books > 1 ):
#     print('You have', books, 'books')
# else:
#     print('You have', books, 'book')
#
# print('You have', books, ('books' if books > 1 else 'book'))


# cost = int(input('fill up your price\n'))
# if cost > 1000:
#     cost = cost - cost * 0.1
#     print('first price:', cost)
# elif cost > 500:
#     cost = cost - cost * 0.05
#     print('second price:', cost)
# elif cost > 100:
#     cost = cost - cost * 0.03
#     print('third price:', cost)


line = input('any line\n \t')
if line:
    print(line)
else:
    print(None)

# ternary
print(line if line else None)