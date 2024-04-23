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

# Calculate the integral of a function
def calculate_integral(lower_limit, upper_limit, function):
    step = 0.001  # Step size for numerical integration
    n_steps = int((upper_limit - lower_limit) / step)
    integral = 0.0
    x = lower_limit
    for _ in range(n_steps):
        integral += step * function(x)
        x += step
    return integral

# Log operations
def log_operation(operation, *args):
    with open("calculator_log.txt", "a") as file:
        file.write(f"{operation}({', '.join(map(str, args))})\n")

def calculator():
    print("1. Nemeh")
    print("2. Hasah")
    print("3. Urjih")
    print("4. Huvaah")
    print("5. Integral")
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
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        elif choice == '5':  # Integral 
            try:
                lower_limit = float(input("Dood too: "))
                upper_limit = float(input("Deed too: "))
                expression = input("Function-iig oruulna uu: ")
                function = lambda x: eval(expression)
            except ValueError:
                print("Buruu utga oruulsan baina dahij oroldono uu.")
                continue

            print("Result:", calculate_integral(lower_limit, upper_limit, function))
            log_operation('calculate_integral', lower_limit, upper_limit, expression)
        else:
            print("Baihgui songolt baina dahij songono uu.")

calculator()
