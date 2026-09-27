N = int(input("Введите позицию N: "))

digits = 1          # сколько цифр в числах блока
count = 9           # сколько чисел в блоке (9, 90, 900, ...)
start = 1           # с какого числа начинается блок (1, 10, 100, ...)

while N > digits * count:
    N = N - digits * count
    digits = digits + 1
    count = count * 10
    start = start * 10

# N — позиция внутри блока
number_index = (N - 1) // digits      # индекс числа (0-based)
digit_index = (N - 1) % digits        # индекс цифры внутри числа

number = start + number_index
number_str = str(number)
answer = number_str[digit_index]

print(answer)