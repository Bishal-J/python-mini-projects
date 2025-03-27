def run_calculator():
    print("Calculator====")

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

num1 = int(input("Enter your first number: "))
for key in operations:
    print(key)
operator = input("Pick an operation: ")
num2 = int(input("Enter your second number: "))

answer = operations[operator](num1, num2)

print(f"{num1} {operator} {num2} = {answer}")

choice = input("Type 'Y' to continue calculating with {answer}, or type 'N' " ).lower()

if choice == 'y':
    num1 = answer
