
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Two real solutions:")
    print("x1 =", x1)
    print("x2 =", x2)

elif delta == 0:
    x = -b / (2*a)
    print("One real solution:")
    print("x =", x)

else:
    print("No real solution (delta < 0)")
