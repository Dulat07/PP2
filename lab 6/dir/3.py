import os


path = input()

if os.path.exists(path):
    dir, name = os.path.split(path)

    print(f"Directories path :{dir}\t\nFile name: {name}")
else:
    print("Path does not exist")