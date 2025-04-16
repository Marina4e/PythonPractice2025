# temperature = 1
#
# if temperature < 10:
#     print("вдягаєте шапку")
# else:
#     print("Не вдягаєте шапку")

# input()

# animal = input('Fill up your animal')
# # print(type(animal))
#
# if animal == 'cat':
#     print('Meo')
# elif animal == 'dog':
#     print('Wof')
# elif animal == 'snake':
#     print('Shshsh')
# else:
#     print("I don't know this animal")

# user_name = input('Fill up your name \n')
# user_age = int(input('Fill up your age please \n'))
# user_age = int(user_age)
# print('user_age', type(user_age))

# if user_name == 'Mark' and user_age >= 21:
#     print('Hello Mark')
#     print('your age is more then 21')
# elif user_name == 'Bob' or user_age < 21:
#     print('hello young guy')
# else:
#     print(f'Hello dear user {user_name}')

user_name = input('Fill up your user name')
if len(user_name) > 9:
    print('Your name is too long')