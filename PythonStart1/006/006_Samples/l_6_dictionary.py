# Creating dict
example_dict = {'key': 'value'}

print(example_dict['key'])

print(example_dict.get('key'))
print(example_dict.get('not_exist_key'))


capital_cities = {
    'Venezuela': 'Caracas',
    'Nicaragua': 'Managua',
}
# v1
capital_cities = dict(Venezuela='Caracas', Nicaragua='Managua')

#v2
capital_cities = dict(
    [("Venezuela", "Caracas"), ("Nicaragua", "Managua")]
)
#v3
capital_cities = dict([["Ukraine", "Kiev"], ["USA", "Washington"]])
#v4
capital_cities = dict(1 = 'Kiev', USA = 'Washington')  # error should be str

# get value from dict
print(capital_cities['Ukraine'])
print(capital_cities.get('Ukraine'))

# put values in dict

capital_cities['Georgia'] = 'Tbilisi'
capital_cities['Moldova'] = 'Kishinev'
capital_cities['China'] = 'Beijing'

# empty dictionary
cities_year_foundation:dict = {}
cities_year_foundation['Kharkiv'] = 1654
cities_year_foundation['Chuhuiv'] = 1638

cities_year_foundation['Kharkiv'] = {'Year of foundation' :1654, 'Main river': 'Kharkiv'}
# dictionaries support

cities_year_foundation['Kharkiv'] = {'Year of foundation' :1654, 'Main rivers': ['Kharkiv', 'Lopan']}
cities_year_foundation['Kharkiv'] = {'Year of foundation' :1654, 'Main rivers': ['Kharkiv', 'Lopan']}

#del
del cities_year_foundation['Chuhuiv']
print(cities_year_foundation)

# for with dict
for country in capital_cities:
    print(capital_cities[country])

# key with value
for country in capital_cities:
    print(f" {country}: { capital_cities[country]}")

# key with value
for country, capital in capital_cities:
    print(country,  capital)


# Распаковка
first_value, second_value = 1, 2

country, capital = 'Georgia', 'Tbilisi'


capital_cities.clear()  # clear all elements in the dictionary
print(capital_cities)

# items
capital_cities.items()
print(capital_cities)

# pop
print(capital_cities.pop()) # видаляє пару ключ значення зі словника, повертає значення.
print(capital_cities)

# popitem
print(capital_cities.popitem()) # видаляє останню пару ключ значення зі словника, повертає значення. LIFO
print(capital_cities)

# update
capital_cities.update({'Brazil': 'Brasilia'}) #
print(capital_cities)

# values
capital_cities.values() #
print(capital_cities)

# setdefault
capital_cities.setdefault('Romania', 'Bucharest' ) # Повертає значення, або як що ключа немає то повертає значення із аргументу.
print(capital_cities)

# fromkeys
any_dictionary= {}
days_name_list = ['Monday', 'Thuesday', 'Wednesday']
new_dictionary = any_dictionary.fromkeys(days_name_list, 'Day')
print(f'{any_dictionary=}')
print(f'{new_dictionary=}')

