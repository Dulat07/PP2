import os

path = input()
f = open(path)
cnt = 0


for i in f:
    cnt+=1


print(cnt)
f.close()