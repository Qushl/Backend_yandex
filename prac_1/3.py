import random
import string

specials = "!@#$%^&*"

password_chars = []

# Три случайные заглавные буквы
for i in range(3):
    letter = random.choice(string.ascii_uppercase)
    password_chars.append(letter)

# Три случайные цифры
for i in range(3):
    digit = random.choice(string.digits)
    password_chars.append(digit)

# Два случайных спецсимвола
for i in range(2):
    symbol = random.choice(specials)
    password_chars.append(symbol)

# Перемешать все
random.shuffle(password_chars)

# Склеить список в одну строку
password = "".join(password_chars)

print(password)