import re

s = input()

pattern = r"^[A-Z][a-z]*"

if re.fullmatch(pattern , s):
    print("Match found")
else:
    print("No match")