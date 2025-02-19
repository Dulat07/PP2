def genf(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

res = genf(10)
for i in res:
    print(", ".join(map(str, res)))
