# Кодування  тексту у байт код для компьютеру прийняте по ASCII American Standard Code of Information of Interchange
# Рядки  - послідовність символів unicode (utf-8) 8 біт

single_quote_str = 'some single quote str'  # знову для себе
double_quote_str = "some single quote str"
some_long_long_text = """some long, very long text. some long, very long text. 
                some long, very long text. some long, very long text. """

# Послідовні рядки будуть "склеюватись" :
"python" "developer"

# рядкові літерали можуть містити екранування
# \t - символ вертикально табуляции
# \n - символ переноса строки

string_with_tab_and_newline_and_slash_and_double_quote = "tab\t and new \n line and slash \\ and double qoute \" "

# сирі рядки
print(r'\path\to_the_\next\file')
print('\path\to_the_\next\file')

# метод котрий переводить у Юнікод симоволи
ord('a')  # => 97
# Крім того, є зворотній метод
chr(65)  # => 'A'

# Багато символів є у юнікоді і опис у пайтоні може бути різний.
"\N{DOMINO TILE HORIZONTAL-00-00}"

ord("\N{DOMINO TILE HORIZONTAL-00-00}")
chr(127025)

# methods
'some str'.upper()  # => 'SOME STR'
'SOME str'.lower()  # => 'some str'
'some str'.capitalize()  # => 'Some str'
'some str'.title()  # => 'Some Str'
'some str'.count('s')  # => 2
# замінює перший аргумент на другий н разів.
'some str'.replace('s', 'm', 1)  # замінює перший аргумент на другий н разів.
#  => 'some str'

'SoMe StR'.swapcase()  # => 'sOmE sTr'

# методи вирівнювання
'some str'.ljust(17, '#')  # => 'some str#########'
'some str'.rjust(17, '#')
'some str'.center(17, '#')

# методи видалення
'#####some str####'.lstrip('#')  # => 'some str####'
'#####some str####'.rstrip('#')
'#####some str####'.strip('#')

# методи розділення
'#####some str####'.split()  # => ['#####some', 'str####']

'file.name.zip'.rsplit('.', 1)  # => ['file.name', 'zip']
# а як що немає розширення?
'file.name.zip.bip'.partition('.')  # => ('file', '.', 'name.zip.bip')
'file.name.zip.bip'.rpartition('.')  # => ('file.name.zip', '.', 'bip')

# За допомогою Join можливо зʼєднати любу послідовність рядків.
"".join('Hello my Dear friend'.split())

# Оператор
'itvdn' in 'I\'am itvdn student'

# Пошук підрядка
'I\'am itvdn student'.find('itvdn')  # => 5
'I"am itvdn student'.find('itvdn', 3, 20)

# замена подстроки
'Student of the Python course'.replace('Student', 'Hard working Student')
'Student of the Python course Student'.replace('Student', 'Hard working Student', 1)

# old
print("Hello dear %s %s your age is %d" % ('Mark', 'Dillan', 44))

name = 'Mark'
surname = 'Dillan'
age = 44

print("Hello dear %s %s your age is %d" % (name, surname, age))


# popular
print("Hello dear {0} {1} your age is {2}".format('Mark', 'Dillan', 44))
name = 'Mark'
surname = 'Dillan'
age = 44
print("Hello dear {0} {1} your age is {2}".format(name, surname, age))


# new
name = 'Mark'
surname = 'Dillan'
age = 44
print(f"Hello dear {name} {surname} your age is {age}")



# обʼєкт рядка не змінюваний.
name = 'igor'
print(id(name))
name = 'Igor'
print(id(name))