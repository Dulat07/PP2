def genf(n):
    for i in range(1, n + 1):
        yield i * i

res = genf(10)

for i in res:
    print(i, end = " ")