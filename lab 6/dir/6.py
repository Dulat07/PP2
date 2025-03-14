import os

path = input()
ch ='A'

while ch != 'Z':
    file = open(f"{ch}.txt", 'w')
    ch = chr(ord(ch)+1)
    file.close()






