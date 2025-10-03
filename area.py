from pydoc import cli


x = input("Enter area of shape: circle, square, rectangle, triangle: ")
x = x.lower()


def circle(r):
    return 3.14 * r * r


def square(a):
    return a * a


def rectangle(c, d):
    return c * d


def triangle(b, h):
    return 0.5 * b * h


if x == "circle":
    r = float(input("Radius: "))
    print(f"The area of the circle is {circle(r): .2f}")

if x == "square":
    a = float(input("Side length: "))
    print(f"The area of the square is {square(a): .2f}")

if x == "rectangle":
    c = float(input("Length: "))
    d = float(input("Width: "))
    print(f"The area of the rectangle is {rectangle(c, d): .2f}")

if x == "triangle":
    b = float(input("base: "))
    h = float(input("height: "))
    print(f"The area of the triangle is {triangle(b, h): .2f}")
