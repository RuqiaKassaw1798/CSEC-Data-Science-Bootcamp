def calculate(a, b, operator):
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Error: Division by zero"
    }
    return operations.get(operator, "Error: Invalid operator")

def get_number(prompt):
    # Helper function to ensure the user enters a valid number.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# --- Improved CLI Interface ---
print("--- Robust CLI Calculator ---")
num1 = get_number("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ").strip()
num2 = get_number("Enter second number: ")

result = calculate(num1, num2, operator)
print(f"\n>>> Result: {result}")