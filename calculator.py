

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
}    


def run_calculator():
    should_accumulate = True
    num1 = float(input("Enter your first number: "))

    while should_accumulate:
        for key in operations:
            print(key)
        operator = input("Pick an operation: ")
        num2 = float(input("Enter your second number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        choice = input("Type 'Y' to continue calculating with {answer}, or type 'N' to exit." ).lower()

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print('\n' * 20)
