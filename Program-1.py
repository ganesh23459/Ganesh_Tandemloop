class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
op = input("Enter operation (add, subtract, multiply, divide): ")
calc = Calculator(a, b, op)
result = calc.calculate()
print("Result:", result)
