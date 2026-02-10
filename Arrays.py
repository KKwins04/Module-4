import array as arr

#Create an array
array_num = arr.array("i", [1,5,3,9,3,7,4])
print("Original array: "+str(array_num))

#Count number of occurences
print("Number of qccurences of number 3 in the said array: "+str(array_num.count(3)))

#Reverse the array
array_num.reverse()
print("Reverse the order of the items")
print(str(array_num))