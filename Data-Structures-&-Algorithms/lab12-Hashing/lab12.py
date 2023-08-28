# Hafsah Shahbaz
# 251684784
# Question 1
# Write a program to implement the hash table. Hash table size is 11. Following is the formula of hash function
# h(i) = (3i+5) mod 11
# Collision should be handled by chaining.
# Test your programs for the following values. 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, and 5
# Finally, print the hash table.



class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

hash_list = []
data = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

for i in range(11):
    hash_list.append(None)


for x in data:
    index = (3*x+5) % 11
    if hash_list[index] == None:
        hash_list[index] = Node(x)
    else:
        chain = Node(x)
        temp = hash_list[index]
        while temp.next is not None:
            temp = temp.next
        temp.next = chain


# To print
for count, val in enumerate(hash_list,1):
    if val is None:
        print(count ,':', end = '')
    else:
        print(count ,':', val.data,'', end='')
        temp = val
        temp = temp.next
        while temp is not None:
            print(temp.data,'', end='')
            temp = temp.next
    print()





