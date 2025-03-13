def count(a):
    upper = 0
    lower = 0
    for i in a:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper,lower

a = input()
upp,low = count(a)
print(f"Uppercase letters: {upp}, Lowercase letters: {low}")