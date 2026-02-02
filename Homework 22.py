#Initialise dictionary
test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

#Printing the original dictionary
print("The original dictionary : ", str(test_dict))

#Initialise value
frequency = int(input("Please enter the value that you want to check: "))

#Using loop
#Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == frequency:
        res = res + 1

#Printing result
print('Frequency of', frequency, 'is: ', str(res))