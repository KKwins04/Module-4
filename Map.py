# Add two lists using map and lambda
numbers1 = [1, 6, 9]
numbers2 = [4, 7, 2]

result = map(lambda x, y: x + y, numbers1, numbers2)

print("Addition of two lists")
print(list(result))


# Using map
nums = [5, 6, 7, 8, 9]

def sq(n):
    return n * n

square = list(map(sq, nums))

print("Square of numbers in list")
print(square)
