import re

s = input()

formatted_string = re.sub(r"(?<!^)(?=[A-Z])", " ", s)

print(formatted_string)
