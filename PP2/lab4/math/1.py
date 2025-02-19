import math

def radian_convert(degree):
    return degree * (math.pi / 180)

x = int(input("Degree to radian:"))
print(radian_convert(x))