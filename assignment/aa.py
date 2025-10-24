def calculator():
    print("🧮 Welcome to the Simple Calculator!")

    while True:
        try:
            # Ask the user for two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values only.")
            continue  # restart loop if input is invalid

        # Ask the user to choose an operation
        print("\nChoose an operation:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")
        print("q : Quit")

        operation = input("Enter your choice (+, -, *, /, q): ").strip()

        if operation == '+':
            result = num1 + num2
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"✅ Result: {num1} × {num2} = {result}")
        elif operation == '/':
            try:
                result = num1 / num2
                print(f"✅ Result: {num1} ÷ {num2} = {result}")
            except ZeroDivisionError:
                print("❌ Error: Division by zero is not allowed!")
        elif operation.lower() == 'q':
            print("👋 Thank you for using the calculator. Goodbye!")
            break
        else:
            print("❌ Invalid operation! Please choose +, -, *, /, or q to quit.")

        print("\n----------------------------\n")