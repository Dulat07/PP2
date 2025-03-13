def check(a):
    a = a.lower()
    return a == a[::-1]
a = input()
res = check(a)
print(res)