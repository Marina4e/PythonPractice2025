# list - впорядкована змінювана послідовність
# 1 variant of creation
my_list = [1, 2, 3]

# 2 variant of creation
my_list = list('abcd')
print(my_list)
print(my_list[0])

# elements in the list
regions: list = ['АР Крим', 'Вінницька', 'Волинська', 'Дніпропетровська', 'Донецька', 'Житомирська', 'Закарпатська',
                 'Запорізька',
                 'Івано-Франківська', 'Київська', 'Кіровоградська', 'Луганська', 'Львівська', 'Миколаївська', 'Одеська',
                 'Полтавська',
                 'Рівненська', 'Сумська', 'Тернопільська', 'Харківська', 'Херсонська', 'Хмельницька', 'Черкаська',
                 'Чернівецька', 'Чернігівська']
counter = 1
for region in regions:
    print(f'{counter}: {region} ')
    counter += 1

# methods
# append додавати
shopping_list = ['milk', 'bread']
shopping_list.append('egs')
print(shopping_list)

# clear очищати
shopping_list = ['milk', 'bread']
shopping_list.clear()
print(shopping_list)

# extend розширити
shopping_list_for_weekly = ['milk', 'bread']
shopping_list_for_tuesday = ['egs', 'potatoes']
shopping_list_for_weekly.extend(shopping_list_for_tuesday)  # shopping_list_for_weekly+= shopping_list_for_tuesday
print(shopping_list_for_weekly)

# index
shopping_list_for_weekly.index('egs')