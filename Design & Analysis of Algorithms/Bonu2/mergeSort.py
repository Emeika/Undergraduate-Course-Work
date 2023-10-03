#Merge Sort :: At each recursive level, Divide your data elements into 3 almost equal parts (arms)

#p-----------mid1---------------mid2----------------r

def Merge_Sort(arr, p, r):
    if (p < r):
        mid1 = p + (r - p) // 3
        mid2 = p + 2 * (r - p) // 3
        Merge_Sort(arr, p, mid1)
        Merge_Sort(arr, mid1 + 1, mid2)
        Merge_Sort(arr, mid2 + 1, r)
        Merge(arr,p, mid1, mid2, r)

def Merge(arr, p, mid1, mid2,r):
    temp = [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = k = p   # start index
    j = mid1 + 1
    s = mid2 + 1
    while( (i<=mid1) and (j<=mid2) and (s<=r) ):   #3 subsets not ended
        if (arr[i] <= ( arr[j] and arr[s] ) ):
            temp[k] = arr[k]
            k+=1
        elif (arr[j] <= ( arr[j] and arr[i] ) ):
            temp[k] = arr[j]
            k+=1
            j+=1
        else:
            temp[k] = arr[s]
            k+=1
            s+=1

    while (i<=mid1):
        temp[k] = arr[i]
        k+=1
        i+=1

    while (j<=mid2):
        temp[k] = arr[j]
        k+=1
        j+=1   

    while (s<=r):
        temp[k] = arr[s]
        k+=1
        s+=1

    for i in range(p,r):
        arr[i] = temp[i]

arr = [38, 27, 43, 3, 9, 82, 10] #5 6 7 11 12 13 
Merge_Sort(arr, 0, 6)