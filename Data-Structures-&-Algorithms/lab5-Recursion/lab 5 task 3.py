# Task 3

#Given an array of integers a, returns a new array obtained from a by replacing each negative
#integer with 0. Also compute time complexity.
#For example, the call negativesToZero({1,-2, 3, 4, -5}), should return the array {1, 0, 3, 4,
#0}

def neg(list,newlist):
    if list == []:
        return list
    elif list[0] < 0:
        newlist.append(0)
    elif list[0] > 0:
        newlist.append(list[0])


    return neg(list[1:],newlist)
    return newlist
newlist = []
print(neg([-4,6,2,-3,-5],newlist))