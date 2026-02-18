# Get range from user
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Create list of squares
squares = [num**2 for num in range(start, end + 1)]

# Separate even and odd square values
even_squares = [num for num in squares if num % 2 == 0]
odd_squares = [num for num in squares if num % 2 != 0]

# Display results
print("Square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
