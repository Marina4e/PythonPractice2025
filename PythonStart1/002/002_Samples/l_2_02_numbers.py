# int
# :int typing або типізація у Python

x_10: int = 15  # десяткове число => 15
y_1: str = bin(15)  # '0b1111' двійкове число або бітове
y_2: int = 0b1111  # двійкове число => 15
z_8: int = 0o17  # вісімкове число => 15
w_16: int = 0xF  # шістнадцяткове число => 15

# операції з цілими числами
sum_x_y = 1 + 2
minus_x_y = 1 - 2
mult_x_y = 1 * 2
quotient = 1 / 2
floored_quotient = 11 / 2  # => 5
remainder = 11 % 2  # => 1
2 + 3 * 4  # => 14
(2 + 3) * 4  # => 20

# float
x: float = 5.5  # Стандартна форма запису => 5.0
y: float = 5.  # Без дробової частини => 5.0
z: float = 3e-4  # Експонентна форма => 0.0003

# Операції
sum_x_y: float = 0.4 + 0.2  # => 0.6000000000000001 ????
some_dif: float = 6 - 3.4
some_sum1: float = 6 + 3.0
some_div1: float = 10 / 3  # => 3.3333333333333335
some_div2: float = 9 / 3  # => 3.0
some_sum2: int = 43 + 34
some_mult: int = 43 * 2

# Декілька корисних функцій при роботі з числами
absolute_n = abs(-5)  # Абсолютне значення / Значення по модулю
rounded_n1: int = round(4.23121)  # round => 4
rounded_n2: float = round(4.23121, 2)  # round => 4.23
fl_n: float = float(45)  # => 45.0
int_from_float: int = int(45.90757820)  # => 45

# нуль може бути і float.
zero: int = 0
zero_float: float = 0.0

# Float vs Decimal

print(0.1 + 0.1 + 0.1 == 0.3)  # not equal



from decimal import Decimal

decimal_value = Decimal('0.1')  # use in string format.

# перевіряємо змінний обʼєкт чи ні.
age: int = 23
print(id(age))
age: int = 24
print(id(age))
