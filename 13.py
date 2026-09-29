n1 = float(input("Enter the first number: "))
op = input("Enter an operator (+, -, *, /): ")
n2 = float(input("Enter the second number: "))

if op == '':
    print("Error: No operator provided")
elif op == '+':
    result = n1 + n2
    print(f"The result of {n1} {op} {n2} is: {result}")
elif op == '-':
    result = n1 - n2
    print(f"The result of {n1} {op} {n2} is: {result}")
elif op == '*':
    result = n1 * n2
    print(f"The result of {n1} {op} {n2} is: {result}")
elif op == '/':
    if n2 == 0:
        print("Error: Division by zero")
    else:
        result = n1 / n2
        print(f"The result of {n1} {op} {n2} is: {result}")
else:
    print("Error: Unknown operator")