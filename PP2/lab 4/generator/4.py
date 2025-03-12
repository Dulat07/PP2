def genf(n,m):
    for i in range(n, m + 1):
        yield i ** 2

n = int(input())
m = int(input())

res = genf(n,m)

for i in res:
    print(i, end = " ")
