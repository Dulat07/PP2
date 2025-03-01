import re

s = input()

pattern = r"^[a].*[b]$"

if re.fullmatch(pattern , s):
    print("Match found")
else:
    print("No match")