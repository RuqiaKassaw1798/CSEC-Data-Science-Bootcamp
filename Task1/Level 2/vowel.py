# Accept a string input from the user
text = input("Enter a string: ")

# this defines the vowels we are looking for in the string
vowels = "aeiouAEIOU"

# Initialize a counter
count = 0

# the loop checks through each character in the string
for s in text:
    if s in vowels:
        count += 1

# Print the result
print(f"The number of vowels in the string is: {count}")