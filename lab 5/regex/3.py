import re

s = input()

pattern = r"^[a-z]+_[a-z]+$"
if re.fullmatch(pattern, s):
    print("Match found")
else:
    print("No match")