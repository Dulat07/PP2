import math

def degree(deg):
    return deg * (math.pi / 180)

deg = int(input())

radian = degree(deg)

print(f"Output radian: {radian:.6f}")
