import os

path = input()
flag = True



if os.path.exists(path):
    print('Existence:', os.access(path, os.F_OK))
    print('Readability:', os.access(path, os.R_OK))
    print('Writability:', os.access(path, os.W_OK))
    print('Executability:', os.access(path, os.X_OK))
    flag = False

else:
    print("Path does not exist")


with open(path) as file:
    if flag == False:
        os.remove(path)

