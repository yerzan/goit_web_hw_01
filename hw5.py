def calculator():
    num1 = float(input("Enter a first number >>> "))

    operation = input("Enter a operation like (+, -, *, /) >>> ")

    num2 = float(input('Enter a second number >>> '))

    if operation == '+':
        result = num1 + num2
        print(f"Result is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result is {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result is {result}")
    elif operation == "/":
        if num2 == 0:
            print('Error. Division by 0 is impossible')
        else:
            result = num1 / num2
            print(f'Result is {result}')

calculator()
