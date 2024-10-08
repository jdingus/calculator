class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return a ** 0.5

    def clear(self):
        self.memory = 0


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


#
def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4", "5"):
            try:
                if choice == "5":
                    num = get_number("Enter a number: ")
                    result = calc.square_root(num)
                    print(f"Result: √{num} = {result}")
                else:
                    num1 = get_number("Enter first number: ")
                    num2 = get_number("Enter second number: ")
                    if choice == "1":
                        result = calc.add(num1, num2)
                        print(f"Result: {num1} + {num2} = {result}")
                    elif choice == "2":
                        result = calc.subtract(num1, num2)
                        print(f"Result: {num1} - {num2} = {result}")
                    elif choice == "3":
                        result = calc.multiply(num1, num2)
                        print(f"Result: {num1} * {num2} = {result}")
                    else:
                        result = calc.divide(num1, num2)
                        print(f"Result: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
