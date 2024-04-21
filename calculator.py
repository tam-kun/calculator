import math

# Nemeh
def add(x, y):
    return x + y

# Hasah
def subtract(x, y):
    return x - y

# Urjih
def multiply(x, y):
    return x * y

# Huvaah
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

#logarithm suuri 10
def logarithm(x):
    if x <= 0:
        return "Invalid input"
    return math.log10(x)

#log operations
def log_operation(operation, x, y=None):
    with open("calculator_log.txt", "a") as file:
        if y is None:
            file.write(f"{operation}({x}) = {eval(operation + '(x)')}\n")
        else:
            file.write(f"{x} {operation} {y} = {eval(operation + '(x, y)')}\n")

def calculator():
    print("1. Nemeh")
    print("2. Hasah")
    print("3. Urjih")
    print("4. Huvaah")
    print("5. Logarithm (suuri 10)")
    print("0. Garah")

    while True:
        choice = input("Ali function songoh ve?: ")

        if choice == '0':
            print("Toonii mashin ashiglasand bayrlalaa")
            break

        if choice in ['1', '2', '3', '4']:  # Operations with two arguments
            try:
                num1 = float(input("Ehnii toogoo oruulna uu: "))
                num2 = float(input("Hoyrdoh toogoo oruulna uu: "))
            except ValueError:
                print("Buruu toogoo oruulsan baina dahij oroldono uu")
                continue

            if choice == '1':
                log_operation('add', num1, num2)
                print("Result:", add(num1, num2))
            elif choice == '2':
                log_operation('subtract', num1, num2)
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                log_operation('multiply', num1, num2)
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                log_operation('divide', num1, num2)
                print("Result:", divide(num1, num2))
        elif choice == '5':  # Logarithm operation
            try:
                num = float(input("Toogoo oruulna uu: "))
            except ValueError:
                print("Buruu too oruulsan baina dahij oroldono uu.")
                continue

            log_operation('logarithm', num)
            print("Result:", logarithm(num))
        else:
            print("Baihgui songolt baina dahij songono uu.")

calculator()
