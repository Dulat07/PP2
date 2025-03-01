import re

s = input()

new_string = re.sub(r"[ ]",",", s)
print(new_string)