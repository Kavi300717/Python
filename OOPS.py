class SmartCalculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def sub(self, a, b):
        result = b - a
        self.history.append(f"{b} - {a} = {result}")
        return result
    
    def mul(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def div(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Error (Division by Zero)")
            return "Cannot divide by Zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def show_history(self):
        print("Calculator History :")
        for record in self.history:
            print(record)

calc = SmartCalculator()
while True:
    print("\nChoose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History ")
    print("6. Exit")

    choice = input("Enter your Choice(1-6) :")

    if choice == '6':
        print("Exiting the calculator!!!")
        break
    elif choice == '5':
        calc.show_history()
    
    elif choice == ['1', '2', '3', '4']:
        try:
            a = float(input("Enter the first number :"))
            b = float(input("Enter the second number :"))
        except ValueError:
            print("Please enter avallid number")
            continue

        if choice == 1:
            print("Result", calc.add(a,b))
        elif choice == '2':
            print("Result", calc.sub(a,b))
        elif choice == '3':
            print("Result", calc.mul(a,b))
        elif choice == '4':
            print("Result", calc.div(a,b))
    else:
        print("Invalid choice. Please select between 1 to 6.")

