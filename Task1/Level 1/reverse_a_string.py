# Accept a string input from the user
text = input("Please enter the string you want to reverse: ")

# Reverse the string using the slicing method
reversed_text = text[::-1]

# Display the results
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")