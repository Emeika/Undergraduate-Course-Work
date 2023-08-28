#task 1
                                                                                                                                                           
'''
def element_place(a,b):
    print(b.index(a))
element_place('apple',['pear', 'orange', 'apple', 'grapefruit'])
'''

#task 2

'''
first_names = ['hafsah', 'kiran', 'daim', 'furqan']
last_names = ['shahbaz', 'qaiser', 'khalid', 'sikander']
def name_generate(x,y,value):
    import random
    for i in range(value):
        name1 = random.randint(0,value)
        name2 = random.randint(0,value)
        print(x[name1] + " " + y[name2])
name_generate(first_names, last_names, 2)
    
'''

#task 3

'''
lis1 = [1,2,3,4]
lis2 = ['a', 'b', 'c', 'd']
def combine(lis1,lis2):
    newlis = tuple(zip(lis1,lis2))
    print(newlis)
combine(lis1,lis2)
'''

#task 4

'''
lists = [1, 4, -2, 8, 4, -9, 3, -24]
def remove_neg(lists):
    for num in lists:
        if num < 0:
            lists.remove(num)
    print(lists)
remove_neg(lists) 
'''

#task 5

'''
def min_max(num):
    for x in num:
        if x == min(num):
            print("minimum number is:" , x , "index is: " , num.index(x) )
        if x == max(num):
            print("maximum number is:" , x , "index is : ", num.index(x) )
min_max([1,3,0,54,23,22,65,24])
'''

#dictionaries
#task 1


p_dictionary={"daim":"030000" , "manal":"0300000" , "bob":"0300000" , "rob":"0300000", "m":"0300000", "anal":"0300000", "lima":"0300000", "sam":"0300000" , "ann":"0300000", "liz":"0300000"}
print(p_dictionary)



#task 2


def add(dicta,name,phone):
    dictb = {name:phone}
    dicta.update(dictb)
    print(dicta)

add(p_dictionary , "abby" , "0546446")

#task 3
def add(dicta, name, phone):
    if name in dicta:
        print("already exists")
    else:
        print("added")
add(p_dictionary, "sam", "055644546")
add(p_dictionary,"mini","0224151024")


#task 4

def delete(dicta,name):
    if name in dicta:
        dicta.pop(name)
        print("deleted")
    else:
        print("not found")
delete(p_dictionary,"kiki")
delete(p_dictionary,"xon")
            

































































