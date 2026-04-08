#  Get the number of terms from the user & help the user what is he asked for
n = int(input("How many Fibonacci numbers do you want? "))

# we Initialize the first two numbers
a, b = 0, 1

# we Use a loop to calculate and print the sequence
for i in range(n):
    if i < n - 1:
        print(a, end=", ")
    else:
        print(a)
    
    a, b = b, a + b