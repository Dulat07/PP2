def genf(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

res = genf(100)

for i in res:
    print(i, end = " ")

