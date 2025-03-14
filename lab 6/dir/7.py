import os


path = input()
str = """"""
with open(path, 'r') as file:
    text = file.read()


str+=text

f = open("file.txt", 'w')
f.write(str)
f.close()

