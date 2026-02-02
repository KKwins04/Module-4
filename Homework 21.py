# Given tuples
tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)

# Function to calculate product of tuple elements
def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

# Calculate products
product1 = tuple_product(tuple1)
product2 = tuple_product(tuple2)

# Display results
print("Tuple 1:", tuple1)
print("Product of Tuple 1:", product1)

print("Tuple 2:", tuple2)
print("Product of Tuple 2:", product2)
