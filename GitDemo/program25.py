import math

a = float(input("Enter a side : "))
b = float(input("Enter a side : "))
c = float(input("Enter a side : "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The area is {area}.")