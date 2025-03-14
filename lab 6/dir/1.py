import os


path = input()

for (root,dirs,files) in os.walk(path,topdown=True):
  print("Directory Names: %s"%dirs)
  print("Files Names: %s"%files)