# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Validate input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0  # Initialize row counter

    # Outer loop using while to handle rows
    while row < size:
        # Inner loop using for to print asterisks in a row
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after a full row is printed
        row += 1

