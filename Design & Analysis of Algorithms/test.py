#DIVIDE AND CONQUER:
def alter(Arr, p, r,size):
    if p==r:
        if Arr[p] % 2 == 0:
            Arr[p] =  Arr[p] + 3
        if (p % 2 == 1) and (p < size/5):
            Arr[p] = Arr[p] + 2
    else:
        mid = (p + r)//2
        alter(Arr, p, mid, size)
        alter(Arr, mid+1, r, size)
    return Arr
lit = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,11]
print("add 3 in all even numbers and add 2 in all odd indices in the first 1/5th elements: ")
print(alter(lit, 0, len(lit)-1, len(lit)))