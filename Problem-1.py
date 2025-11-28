
class Calculator:
    def calculate(self, a, b, op):
        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        else:
            return "Invalid operation"

calc = Calculator()
print(calc.calculate(10, 5, "add"))
