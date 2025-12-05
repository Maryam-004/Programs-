a = float(input("Enter a number:"))
b = float(input("Enter a number:"))
c = float(input("Enter a number:"))
d = float(input("Enter a number:"))

max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d

print("The maximum number is :",max)
