# Accept a list of numbers from the user
# We split the string by spaces and convert each part to an integer
numbers = list(map(int, input().split()))

# Check if the list is empty to avoid errors
if not numbers:
    print("The list is empty.")
else:
    # we Assume the first number is the maximum to start
    max = numbers[0]

    # this line of code Iterates through the list to compare numbers
    for num in numbers:
        if num > max:
            max = num

    print(f"The largest number in the list is: {max}")