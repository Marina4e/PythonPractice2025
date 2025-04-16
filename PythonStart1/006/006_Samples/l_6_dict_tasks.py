# Порахувати за допомогою словника скільки разів елемент повторюється у списку.
classmates_name = ['Sergey', 'Igor', 'Tanya', 'Sergey', 'Mikhael', 'Sergey', 'Lena']

# v1
answer = {}

for name in classmates_name:
    if name in answer.keys():
        answer[name] += 1
    else:
        answer[name] = 1
print(answer)

# v2
answer = {}
for name in classmates_name:
    answer[name] = classmates_name.count(name)

print(answer)

# пройдемося за словником, і вивести всі значення, які мають парний ключ.
range_none: dict = dict().fromkeys(range(10))
for k in range_none.keys():
    if k % 2 == 0:  
        print(k)


# Видалити всі ключі, значення яких починається з літери.
#v1 DO NOT delete element in the collection durting cycle
only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
for k in only_int_keys:
    if type(k) == str:
        del only_int_keys[k]

print(only_int_keys)

# v 2

# Видалити всі ключі, значення яких починається з літери.
only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}

copy_only_int_keys = only_int_keys.copy()
for k in only_int_keys:
    if type(k) == str:
        del copy_only_int_keys[k]

print(copy_only_int_keys)
