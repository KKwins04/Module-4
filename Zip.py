# Zip elements of two lists
s1 = {2, 3, 4}
s2 = {'b', 'a', 'c'}

s3 = list(zip(s1, s2))
print(s3, "\n")


# Zip elements of two lists but the second list is reversed
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


# Zip into dictionary
stocks = ['reliance', 'info', 'tcs']
prices = [4321, 5437, 2670]

new_dict = {stock: price for stock, price in zip(stocks, prices)}
print("\n", new_dict)
