some_set = {'a', 'b', 'c', 'c'}
some_set1 = set(['one', 'two', 'three', 'four'])
some_set2 = set('aHello')
some_set3 = {'a', 1, 3, 4, 5, 2, 8}
# print(some_set3)
some_frozen_set = frozenset('Frozen')
# print(some_frozen_set)

# колекції
# [], 'line', {'key':'value'}, {1, 2}

# print(len(some_set2))
# print('l' in some_set2)

# some_set3.clear()
# print(some_set3.pop())
# print(some_set3.pop())
# print(some_set3.pop())
# print(some_set3.pop())
# print(some_set3.pop())
# print(some_set3.pop())
# some_set3.discard('any')
# some_set3.remove('a')
# some_set3.add([])
# print(some_set.union(some_set3))
# print(some_set | some_set3 )
# some_set |= some_set3
# print(some_set)

# intersection
# print(some_set.intersection(some_set3, some_set2 ))
# print(some_set & some_set3 & some_set2  )

# print(some_set.difference(some_set3))
# print(some_set.isdisjoint(some_set3))
# print({1, 2, 3}.issubset({1, 2, 3, 4}))
# print({1, 2, 3} <= {1, 2, 3, 4})

# print({1, 2, 3}.symmetric_difference([1, 2, 3, 4]))
# print({1, 2, 3} ^ {1, 2, 3, 4})

# print(bool(set()))

some_tuple = (1, 2, 3)
some_tuple1 = ([], {}, set(), ())
some_tuple2 = tuple(['a', 'b', 'c'])
some_tuple3 = tuple("Hello I am python developer")

# empty tuple
empty_tuple = ()
empty_tuple2 = tuple()

# print(len(some_tuple1))
# print('H' in some_tuple3)
# print(some_tuple3.count('l'), 'count')
# print(some_tuple3.index('l'), 'index')

# print(some_tuple3)

# a, b, c = (1, 2, 3)
# print(a, b, c)

# swapping
a = 1
b = 2

c = a
a = b
b = c
del c
# print(f'{a=} {b=}')

a = 'One'
b = 'Two'
c = 'Three'

a, b, *anything = (b, a, c, 1,3, 4, 'hello')
# print(f'{a=} {b=} {anything=}')

first, *middle, last = ('Igor', 'Mark', 'Lena', 'Zurab')
# print(f'{first=}, {middle=}, {last=}')

class_school = (('Igor', 10), ('Mark', 12), ('Lena', 8), ('Zurab', 11))
for st, mark in class_school:

    print(f'Student:{st}, mark:{mark}')

