import re

s = input("Введите строку: ")


split_string = re.split(r"(?=[A-Z])", s)

print("Результат:", split_string)
