#-----------------------PartA-----------------------#
#BRUTE FORCE:
def alter(Arr, n):

    fifth = n // 5
    for i in range(fifth):
        if Arr[i] % 2 == 0:
            Arr[i] =  Arr[i] + 3
        if i % 2 == 1:
            Arr[i] = Arr[i] + 2
    return Arr
print("add 3 in all even numbers and add 2 in all odd indices in the first 1/5th elements: ")
lit = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11]
print(alter(lit, len(lit)))
#-----------------------PartA-----------------------#
#DIVIDE AND CONQUER:
def alter(Arr, p, r):
    if p==r:
        if Arr[p] % 2 == 0:
            Arr[p] =  Arr[p] + 3
        if p % 2 == 1:
            Arr[p] = Arr[p] + 2
    else:
        mid = (p + r)//2
        alter(Arr, p, mid)
        alter(Arr, mid+1, r)
    return Arr
lit = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11]
fifth = (0 + 30)// 5
print("add 3 in all even numbers and add 2 in all odd indices in the first 1/5th elements: ")
print(alter(lit, 0, fifth))

#-----------------------PartB-----------------------#
#BRUTE FORCE:
def calc_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
print("take sum of n integers")
print(calc_sum([1,2,3,4,5,6,7,8,9]))
#-----------------------PartB-----------------------#
#DIVIDE AND CONQUER:
def calc_sum(arr, p, r):
    if p == r:
        return arr[p]
    elif p == r-1:
        return arr[p] + arr[r]

    
    mid1 = p + (r - p) // 3
    mid2 = p + 2 * (r - p) // 3
    chunk1 = calc_sum(arr, p, mid1)
    chunk2 = calc_sum(arr, mid1 + 1, mid2)
    chunk3 = calc_sum(arr, mid2 + 1, r) 

    return chunk1 + chunk2 + chunk3
print("take sum of n integers & to be divided into three parts")
print(calc_sum([1,2,3,4,5,6,7,8,9], 0, 8))

#-----------------------PartC-----------------------#
#BRUTE FORCE:
def countB(Arr, b):
    freq = 0
    for i in range(len(Arr)):
        if (Arr[i] == b):
            freq+= 1
    return freq
print("Count the total number of B in this sorted list - brute force")
print(countB([1,1,1,1,2,2,3,3,3,4,4,5,5,6,6], 3))
#-----------------------PartC-----------------------#
#INTELLIGENT:
def countB(Arr, b):
    freq = 0
    for i in range(len(Arr)):
        if (Arr[i] == b):
            freq+= 1
        elif (b < Arr[i]):
            return freq
    return freq
print("Count the total number of B in this sorted list - intelligent")
print(countB([1,1,1,1,2,2,3,3,3,4,4,5,5,6,6], 3))
#-----------------------PartC-----------------------#
#DIVIDE AND CONQUER:
def countB(Arr, b, p, r):
    if (p==r and Arr[p] == b):
        return 1
    elif (p==r and Arr[p] != b):
        return 0
    if (Arr[p] == b and Arr[r] == b):
        return r-p+1                   # all B's (sub list or full list)
    if (Arr[r] < b):
        return 0                       # all A's
    if (Arr[p] > b):
        return 0                       # all C's
    else:
        mid = (p+r) //2
        count1 = countB(Arr, b, p, mid)
        count2 = countB(Arr, b, mid+1, r)
    return count1 + count2
print("Count the total number of B in this sorted list - divide n conquer")
print(countB([1,1,1,1,2,2,3,3,3,4,4,5,5,6,6], 3, 0, 14))

#-----------------------PartD-----------------------#
#BRUTE FORCE:
def swap(Arr):

    for i in range(len(Arr)-1):
        temp = Arr[i]
        Arr[i] = Arr[i+1]
        Arr[i+1] = temp
arr = [2,4,8,16]
print("Swap with its immediate neighbor element")
swap(arr)
print(arr)

#-----------------------PartD-----------------------#
#DIVIDE AND CONQUER:
def swap(arr, p, r):
    if p == r:
        arr[p], arr[p + 1] = arr[p + 1], arr[p]
    else:
        q = (p+r) // 2
        swap(arr, p, q)
        swap(arr, q+1, r)
arr = [2,4,8,16]
print("Swap with its immediate neighbor element with divide and conquer:")
swap(arr,0,2)
print(arr)

#-----------------------PartE-----------------------#
#BRUTE FORCE:
def duplicate(T,Z):
    if len(T) != len(Z):
        return False
    for i in range(len(T)):
        if T[i] != Z[i]:
            return False
    return True
print(duplicate([1,2,3],[1,2,3]))