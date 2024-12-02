def calculator():
    while True:
        try:
            print("\nSimple Calculator")
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue
            
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!")
        except ValueError:
            print("Error: Invalid input!")

calculator()