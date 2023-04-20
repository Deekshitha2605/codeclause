import math

def calculator():
    print("Welcome to the calculator!")
    print("Enter 'quit' to exit")
    
    while True:
        user_input = input("Enter an expression: ")

        if user_input == "quit":
            print("Exiting calculator...")
            break

        try:
            if "mod" in user_input:
                op1, op2 = user_input.split("mod")
                result = int(op1) % int(op2)
                print("Result:", result)

            elif "^" in user_input:
                op1, op2 = user_input.split("^")
                result = int(op1) ** int(op2)
                print("Result:", result)

            elif "sqrt" in user_input:
                op = user_input.split("sqrt")[-1].strip()
                result = math.sqrt(int(op))
                print("Result:", result)

            elif "sin" in user_input:
                op = user_input.split("sin")[-1].strip()
                result = math.sin(int(op))
                print("Result:", result)

            elif "cos" in user_input:
                op = user_input.split("cos")[-1].strip()
                result = math.cos(int(op))
                print("Result:", result)

            elif "tan" in user_input:
                op = user_input.split("tan")[-1].strip()
                result = math.tan(int(op))
                print("Result:", result)

            else:
                result = eval(user_input)
                print("Result:", result)

        except (ZeroDivisionError, ValueError, TypeError, AttributeError) as e:
            print("Error:", e)

def main():
    calculator()
    print("Thanks for using our Calculator!")

if __name__ == "__main__":
    main()
