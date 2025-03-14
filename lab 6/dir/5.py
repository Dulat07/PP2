import os


lst = ["Apple", "Banana", "Cherry", "Mango", "Orange"]


with open("aa.txt", "a") as name:
    for i in lst:
        name.write(f'{i}\n\t')



