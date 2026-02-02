#Initialise dictionary
test_dict = {'Codingal' : 9, 'is' : 4, 'best' : 4, 'for' : 6, 'Coding' : 7}

#Printing the original dictionary
print("The original dictionary : ", str(test_dict))

#Initialise value
K = 4

#Using loop
#Selective key values in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

#Printing result
print('Frequency of K is: ', str(res))