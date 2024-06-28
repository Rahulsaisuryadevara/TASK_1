import math

def calculator():
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_choice():
        while True:
            print("\nSelect operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Power")
            print("6. Modulus")
            print("7. Square Root")
            print("8. Recall Last Result")
            print("0. Exit")
            choice = input("Enter choice (0/1/2/3/4/5/6/7/8): ")
            if choice in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                return choice
            else:
                print("Invalid choice. Please choose a valid option.")

    print("Simple Calculator")

    last_result = None

    while True:
        choice = get_choice()
        
        if choice == '0':
            print("Exiting the calculator.")
            break

        if choice == '8':
            if last_result is not None:
                print(f"Last result: {last_result}")
                continue
            else:
                print("No previous result stored.")
                continue

        if choice == '7':
            num1 = get_number("Enter a number: ")
            result = math.sqrt(num1)
            operation = "Square Root"
        else:
            num1 = last_result if last_result is not None and choice == '8' else get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = num1 + num2
                operation = "Addition"
            elif choice == '2':
                result = num1 - num2
                operation = "Subtraction"
            elif choice == '3':
                result = num1 * num2
                operation = "Multiplication"
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation = "Division"
                else:
                    result = "undefined (division by zero)"
                    operation = "Division"
            elif choice == '5':
                result = math.pow(num1, num2)
                operation = "Power"
            elif choice == '6':
                result = num1 % num2
                operation = "Modulus"
            else:
                result = "Invalid input"
                operation = "Invalid operation"
        
        last_result = result
        print(f"\n{operation} result: {result}")

# Run the calculator
calculator()
