List1 = ["apple" ,"banana", "orange", "grape", "kiwi"]

def turntoupper(str1):
    return str1[0].upper() + str1[1:]

List1 = list(map(turntoupper, List1))
print(List1)
