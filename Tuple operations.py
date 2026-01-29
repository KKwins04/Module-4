#Create a tuple with different dtata types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#Create a tuple
tuplex = (4, 6, 7, 4, 2, 0)
print(tuplex)
#Tuples are immutable, so you cannot add new elements
#Using merge of tuples with the +operator you can add an element and it will create a
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 90, 60, 70, 40)
print(tuple1.count(50))

#Create a tuple
tuplex = (2,4,1,3,4,6,7,8,6,1)
#Used tuple[Start:Stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#Is exclusive
print(_slice)
#If start index isnt defined, it is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)