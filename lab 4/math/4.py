import math

def res(length,height):
    return height * length

length = int(input())
height = int(input())

result = res(length,height)

print(f"Area of the parallelogram: {result}")