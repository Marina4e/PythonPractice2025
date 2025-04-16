example_dict = {'key': 'value'}
# print(example_dict['key'])
# print(example_dict.get('key_no_exist'))
# v1
capital_cities = {
   'Venezuela': 'Caracas',
   'Nicaragua': 'Managua',
}

# v2
capital_cities_2 = dict([['Venezuela', 'Caracas'],['Nicaragua', 'Managua']])
# print(capital_cities_2, 2)

# v3
capital_cities_3 = dict(Venezuela='Caracas', Nicaragua='Managua')
# print(capital_cities_3, 3)
# print(capital_cities_3['Venezuela'])

capital_cities['Ukraine'] = 'Kiev'
# print(capital_cities['Ukraine'])

capital_cities['Georgia'] = 'Tbilisi'
capital_cities['Moldova'] = 'Kishinev'
capital_cities['China'] = 'Beijing'

# print(capital_cities)

# empty dictionary
cities_year_foundation = {}
cities_year_foundation: dict = dict()
cities_year_foundation['Kharkiv'] = 1654
cities_year_foundation['Chuhuiv'] = 1638


cities_year_foundation['Kharkiv'] = {'Year of foundation': 1654, 'Main rivers': ['Kharkiv', 'Lopan']}
del cities_year_foundation['Chuhuiv']
# print(cities_year_foundation)

# for with dict
# print(capital_cities)
# v1
# for country in capital_cities:
#    print(country, capital_cities[country])

# v2
# for country, capital in capital_cities.items():
#    print(f'{capital} is the capital or {country}')
   # print(f'{capital=} {country=}')

# print(capital_cities.items())

# for element in [['Venezuela', 'Caracas'], ('Nicaragua', 'Managua'), ('Ukraine', 'Kiev'), ('Georgia', 'Tbilisi'), ('Moldova', 'Kishinev'), ('China', 'Beijing')]:
#   country, capital = element
#   print(country, capital)

# clear
# print(capital_cities, id(capital_cities))
# capital_cities.clear()
# print(capital_cities, id(capital_cities))

# pop

# print(capital_cities.pop('Nicaragua'))
# print(capital_cities)

# # popitem
# print(capital_cities)
# print(capital_cities.popitem())
# print(capital_cities)

# update
brazil = {'Brazil': 'Brasilia'}
capital_cities.update(brazil)
# print(capital_cities)

# values
values_of_capital_cities = capital_cities.values()
# print(values_of_capital_cities)

# keys
keys_of_capital_cities = capital_cities.keys()
# print(keys_of_capital_cities)

# setdefault
# print('GET --',capital_cities.get('Romania'))
# print('SETDEFAULT -- ', capital_cities.setdefault('Romania', 'Default values' )) # Повертає значення, або як що ключа немає то повертає значення із аргументу.
# print(capital_cities)

# fromkeys
empty_dictionary: dict = {}
days_name_list = ['Monday', 'Tuesday', 'Wednesday']
new_dict = empty_dictionary.fromkeys(days_name_list, 'any values')
# print(new_dict)

# task 1
# Порахувати за допомогою словника скільки разів елемент повторюється у списку.
classmates_name = ['Sergey', 'Igor', 'Tanya', 'Mark', 'Sergey', 'Mikhael', 'Sergey', 'Lena', 'Mark']  # вхідні данні

# answer = {}
# for name in classmates_name:
#    if name in answer.keys():
#       answer[name] += 1
#    else:
#       answer[name] = 1
#
# print(answer)

#v2
# answer = {}
# for name in classmates_name:
#    answer[name] = classmates_name.count(name)
#
# print(answer)

# пройдемося за словником, і вивести всі значення, які мають парний ключ.
# data_dict = {22: 'nice age',1: 'one', 33 :'any text',2: 'two',  3: '3', 5: 5, 6: '6', 9: 'end'}
# data_dict = {}.fromkeys(range(40), "Any value")
# for key, value in data_dict.items():
#    if key % 2 == 0:
#       print(value)

# Видалити всі ключі, значення яких починається з літери.
only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
only_int_keys_copy: dict = only_int_keys.copy()
for k in only_int_keys.keys():
   if type(k) == str:
      del only_int_keys_copy[k]

print(only_int_keys_copy)





