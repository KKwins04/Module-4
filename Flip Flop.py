def palind(r):
    end = len(r) -1
    start = 0
    while(start < end):
        if(r[start] != r[end]):
            return False
        start += 1
        end -= 1
    return True
    
        #return r == r[::-1]


r = (1,9,3,4,6,1)

if(palind(r)):
    print("The tuple is flip flop")
else:
    print("The tuple is not flip flop")
