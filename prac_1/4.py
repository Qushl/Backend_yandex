text = input("Введите строку: ").lower()

counts = {}

# символ - его количество в строке
for ch in text:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1

print("Все символы:")
for ch in counts:
    print(ch, "->", counts[ch])

# Находим 3 самых частых
items = list(counts.items()) # Словарь в список пар
items.sort(key=lambda pair: pair[1], reverse=True)
top3 = items[:3]

print("Топ-3 символа:")
for ch, count in top3:
    print(ch, "->", count)