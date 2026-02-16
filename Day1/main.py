def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: modulus by zero"

def km_to_m(km):
    return km * 1000

def km_to_cm(km):
    return km * 100000

def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

def mb_to_gb(mb):
    return mb / 1000

def mb_to_kb(mb):
    return mb * 1000

def triangle_area(base, height):
    return base * height / 2


def square_area(side: int) -> int:
    if side < 0:
        raise ValueError("side must be non-negative")
    return side * side

def circle_area(radius: float) -> float:
    return 3.14 * radius ** 2

# calculator
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = input("Enter the operations like +, -, *, %, /: ")

match input3:
    case "+":
        print(add(input1, input2))
    case "-":
        print(subtract(input1, input2))
    case "*":
        print(multiply(input1, input2))
    case "/":
        print(divide(input1, input2))
    case "%":
        print(modulus(input1, input2))
    case _:
        print("Invalid operation")

# conversion of km to m or cm
km_input = int(input("Enter the distance in km: "))
choice_input = input("Enter the unit of measurement(m, cm) to convert: ")

match choice_input:
    case "m":
        print(km_to_m(km_input))
    case "cm":
        print(km_to_cm(km_input))
    case _:
        print("Invalid unit of measurement")

# conversion of temperature from Celsius to Fahrenheit or kelvin
celsius_input = int(input("Enter the temperature: "))
choice_input_temperature = input("Enter the unit of measurement(F, K) to convert: ")

match choice_input_temperature:
    case "F":
        print(c_to_f(celsius_input))
    case "K":
        print(c_to_k(celsius_input))
    case _:
        print("Invalid unit of measurement")

# conversion of MB into GB, KB
mb_input = int(input("Enter the size in MB: "))
choice_input_size = input("Enter the unit of measurement(GB, KB) to convert: ")

match choice_input_size:
    case "GB":
        print(mb_to_gb(mb_input))
    case "KB":
        print(mb_to_kb(mb_input))
    case _:
        print("Invalid data input")

# area of a triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
print(triangle_area(base, height))

# area of a square
side = int(input("Enter the side of the square: "))
print(square_area(side))

 # area of a circle
radius = float(input("Enter the radius of the circle: "))
print(circle_area(radius))