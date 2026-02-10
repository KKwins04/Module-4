#Different types of sets in python
#Set of integers
my_set ={1,4,3}
print(my_set)

#Set of mixed datatypes
my_set = {1.0, "Hello", (2,1,3)}
print(my_set)

#Set cannot have duplicates
my_set = {4,2,3,4,3,2}
print(my_set)

#We can make a set from a list
my_set = set([3,2,3,2])

#Remove a number from the list
num_set = set([3,4,5])
print("Original set: ", num_set)
num_set.pop()
print("After removing the first element from the said set: ", num_set)