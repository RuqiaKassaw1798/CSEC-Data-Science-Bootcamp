# Accept user input
num = int(input("Enter a number: "))

# Initialize the result variable to 1
factorial = 1

# Logic: Factorials are only for numbers 0 and above
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Multiply numbers from 1 up to 'num'
    for i in range(1, num + 1):
        factorial *= i
    
    print(f"The factorial of {num} is {factorial}")