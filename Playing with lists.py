L = [4,5,45,2,9,7,10,8]
print('Original List: ', L)

#Variable to store sum of list
sum = 0

#Finding the sum
for i in L:
    sum += i

#Divide total elements by number of elements
avg = sum/len(L)

print("sum =", sum)
print("average = ", avg)

#Sorting the elements of the list
L.sort()

#printing the first element
print("Smallest element is: ", L[0])

#printing last element
print('Largest element is: ', L[-1])