# Task 3
# Let’s write a function that simulates shuffling of a deck of cards,
# you are required to store all the
# card faces in a list and generate random permutations of all list elements.
# To achieve our required purpose, we can use Fisher–Yates shuffle Algorithm
# for optimal performance.


faces = []
faces.extend(["Jack" for x in range(4)])
faces.extend(["queens" for x in range(4)])
faces.extend(["kings" for x in range(4)])
print(faces)

import random
list_len = len(faces)

for i in range(list_len -1,1,-1):
    j = random.randint(0,list_len-1)
    faces[i] , faces[j] = faces[j] , faces[i]

print(faces)



#  four jacks, four queens, and four kings
