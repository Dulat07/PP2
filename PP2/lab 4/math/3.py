import math

sides = int(input())
def res(len):
    return int((sides * len**2) / (4 * math.tan(math.pi / sides)))

len = int(input())
result = res(len)

print(f"The area of the polygon is: {result}")