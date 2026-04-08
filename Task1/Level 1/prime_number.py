 
num = int(input("Enter a number: "))
# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        # It runs only if the loop finished without finding a factor
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")