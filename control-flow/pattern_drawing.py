

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for column in range(size):
        print("*", end="")
    print()  # Move to the next line after completing a row
    row += 1
