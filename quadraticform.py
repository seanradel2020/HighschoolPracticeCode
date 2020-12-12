#program will crash if the equation has no real roots

import math

def main():
    print("This program finds the real solutions to a quadratic\n")


    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b*b - 4*a*c
    if discrim < 0:
        print("\nThe equation has no real root!")
    else:
        if discrim == 0:
            root = -b / (2*a)
            print("There is adouble root at", root)
        else:
            print("\nThe equation has no real root!")
            discRoot = math.sqrt(b * b - 4 * a * c)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)


    print("\nThe solutions are:",root1, root2)

main()
