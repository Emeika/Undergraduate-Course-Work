#=============================================
#=============================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section:  C
# Date   : 06/12/22
#=============================================

#=============================================
#  TASK L01: Node class creation
#---------------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        #==================
        # Insert code here:
        self.data = data
        self.prev = prev
        self.next = next

        #------------------
        pass
 
        #==================

#=============================================        

    
#=============================================
#  TASK L02: 
#---------------------------------------------
def TaskL02():

    head = Node(1)            # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------

    n2 = Node(2,head)
    head.next =n2

    n3 = Node(3,n2)
    n2.next = n3

    tail = Node(4,n3)
    n3.next = tail
    
    #------------------
    
    return head               # DO NOT MODIFY THIS LINE
    
#=============================================


#=============================================
#  TASK L03: 
#---------------------------------------------
def TaskL03(head, data):
    
    node = None            # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------

    temp = head

    while temp is not None:
        if temp.data == data:
            node = temp
            break
        temp = temp.next

    #==================

    return node               # DO NOT MODIFY THIS LINE
    
#=============================================


#=============================================
#  TASK L04: 
#---------------------------------------------
def TaskL04(L1, L2):
    #==================
    # Insert code here:
    #------------------
    temp = L1
    while temp.next is not None:
        temp = temp.next
    temp.next = L2
    L2.prev = temp

    #==================
    return L1               # DO NOT MODIFY THIS LINE

    
#=============================================


#=============================================
#  TASK L05: 
#---------------------------------------------
def TaskL05():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------
    head = Node(None)  # set None as the data
    r2 = Node(None)  # set None as the data
    head.next = r2
    r2.prev = head

    #==================
    return head               # DO NOT MODIFY THIS LINE

    
#=============================================



#=============================================
#  TASK L06: 
#---------------------------------------------
def TaskL06():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------
    head = TaskL05()

    c1 = Node(1)
    c2 = Node(2)
    c1.next = c2
    c2.prev = c1
    # c1 acts as the head of the first pink row
    head.data = c1  # NOTE: we're putting the row's head in data
    c1.prev = head
    # Second pink row:
    c3 = Node(3)
    r2 = head.next
    # c3 acts as the head of the second pink row
    r2.data = c3  # NOTE: we're putting the row's head in data
    c3.prev = r2

    #==================
    return head               # DO NOT MODIFY THIS LINE

#=============================================




#=============================================
#  TASK L07: 
#---------------------------------------------
def TaskL07():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------
    head = Node(None)  # set None as the data
    r2 = Node(None,head)  # set None as the data
    head.next = r2

    r3 = Node(None,r2)
    r2.next = r3

    r4 = Node(None,r3)
    r3.next = r4

    c1 = Node(1,head)
    c2 = Node(2,c1)
    c1.next = c2

    c3 = Node(4,r3)
    c4 = Node(5,c3)
    c3.next = c4

    c5 = Node(6,c4)
    c4.next = c5

    c6 = Node(3,r4)


    head.data = c1
    r3.data = c3
    r4.data = c6

    #==================

    return head               # DO NOT MODIFY THIS LINE

#=============================================




#=============================================
#  TASK L08: 
#---------------------------------------------
def TaskL08(head):    
    #==================
    # Insert code here:
    #------------------
    temp = head
    i = 0
    while temp.next is not None:
        if temp.data is not None:
            i += 1
        temp = temp.next
    return i

    #==================

#=============================================




#=============================================
#  TASK L09: 
#---------------------------------------------
def TaskL09(head):    
    #==================
    # Insert code here:
    #------------------
    greentemp = head
    pinktemp = None
    i = 0
    while greentemp is not None:
        if greentemp.data is not None:
            pinktemp = greentemp.data
            while pinktemp is not None:
                i += 1
                pinktemp = pinktemp.next

        greentemp = greentemp.next

    return i

    #==================

#=============================================



#=============================================
#  TASK L10: 
#---------------------------------------------
def TaskL10(head, node, currentRow):
    '''
    Parameters:
    -----------
        head - the root reference of the entire nested structure
        node - the random node in a row to begin with
        currentRow - Reference of the GREEN node that contains this row
    '''

    rowHead = None              # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------
    pass
    #==================

    return rowHead              # DO NOT MODIFY THIS LINE

#=============================================

head = TaskL02()
print(head.data)

n2 = head.next
print(n2.data)

print(head.next.next.data)
print(n2.next.data)
print(head.next.next.prev.data)
print(head.next.next.next.next)

print(head.next.next.prev.next.prev.next.prev.next.prev.next.prev.data)


