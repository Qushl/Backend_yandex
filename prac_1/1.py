celsius = float(input("Введите температуру в °C: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

#Вывод с округлением до 2 знаков после запятой ":.2f"
print(f"{celsius}°C = {fahrenheit:.2f}°F") 
print(f"{celsius}°C = {kelvin:.2f}K")