#=============================================
#=============================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section: C
# Date   : 29/11/2022
#=============================================



#---------------------------------------------


#=============================================
#  TASK S01: Basic Stack Operations
from Stack import Stack
from CircularQueue import CircularQueue

def TaskS01():
    S = Stack()             # DO NOT MODIFY THIS LINE
    #==================
    # Insert code here:
    S.push(6)
    S.push(7)
    S.push(9)
    S.pop()
    S.top()
    S.pop()
    S.push(10)
    S.pop()
    S.pop()
    S.push(20)
    #------------------
    pass
    #==================
    return S                # DO NOT MODIFY THIS LINE 




#=============================================
#  TASK S01: Basic Queue Operations
#---------------------------------------------
def TaskQ01():
    Q = CircularQueue()     # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(9)
    Q.dequeue()
    Q.first()
    Q.dequeue()
    Q.enqueue(10)
    Q.dequeue()
    Q.dequeue()
    Q.enqueue(20)

    #------------------
    pass
    #==================
        
    return Q                # DO NOT MODIFY THIS LINE 


#=============================================
#  TASK L01: Node class creation
#---------------------------------------------
class Node:
    def __init__(self, data, next=None):
        #==================
        # Insert code here:
        self.data = data
        self.next = next
        #------------------
        pass
        #==================


#=============================================
#  TASK L02: 
#---------------------------------------------
def TaskL02():
    #==================
    # Insert code here:
    #------------------
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    #==================
    
    return (n1,n2,n3)       # DO NOT MODIFY THIS LINE


#=============================================
#  TASK L03: 
#---------------------------------------------
def TaskL03():
    n1 = Node(1)            # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    n2 = Node(2)
    n1.next = n2
    #------------------
    #
    pass
    #==================
    
    return n1               # DO NOT MODIFY THIS LINE
    

    
#=============================================
#  TASK L04: 
#---------------------------------------------
def TaskL04():
    n1 = Node(6)            # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    n2 = Node(5)
    n1.next = n2

    n3 = Node(4)
    n2.next = n3

    n4 = Node(3)
    n3.next = n4

    n5 = Node(2)
    n4.next = n5
    #------------------
    pass
    #==================
    
    return n1               # DO NOT MODIFY THIS LINE
    
    
    
    
    
#=============================================
#  TASK L05: 
#---------------------------------------------
def TaskL05(head):
    
    sum = 0                 # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------
    temp = head
    while temp != None:
        sum += temp.data
        temp = temp.next
    #------------------
    
    return sum              # DO NOT MODIFY THIS LINE
    
    
    
    
#=============================================
#  TASK L06: 
#---------------------------------------------
def TaskL06(head, node):
    #==================
    # Insert code here:
    node.next = head
    head = node
    #------------------
    pass
    #------------------

    return head               # DO NOT MODIFY THIS LINE

    
    
#=============================================
#  TASK L07: 
#---------------------------------------------
def TaskL07(head):
    #==================
    # Insert code here:
    head = head.next
    #------------------
    pass
    #------------------

    return head               # DO NOT MODIFY THIS LINE
    
    
    
    
#=============================================
#  TASK L08: 
#---------------------------------------------
def TaskL08(head):
    tail = None               # DO NOT MODIFY THIS LINE
    #==================
    # Insert code here:
    temp = head
    while temp.next != None:
        temp = temp.next

    tail = temp


    #------------------
    pass
    #------------------

    return tail               # DO NOT MODIFY THIS LINE
    



#=============================================
#  TASK L09: 
#---------------------------------------------
def TaskL09(head, node):
    #==================
    # Insert code here:
    tail = TaskL08(head)
    tail.next = node

    #------------------
    pass
    #------------------



    
#=============================================
#  TASK L10: 
#---------------------------------------------
def TaskL10(head):
    #==================
    # Insert code here:
    if head is not None:
        if head.next == None:
            head = None
        else:
            temp = head
            while temp.next.next != None:
                temp = temp.next
            tempo = temp.next
            temp.next = None
            tempo = None

    #------------------
    pass
    #------------------


    
#=============================================
#  TASK L11: 
#---------------------------------------------
def TaskL11(head,k):
    #==================
    # Insert code here:
    if k == 0:
        head = head.next
    else:
        i = 0
        slow = None
        temp = head

        while i is not k:
            slow = temp
            temp = temp.next
            i += 1
        slow.next = temp.next
        temp.next = None


    #------------------
    pass
    #------------------
    
    return head               # DO NOT MODIFY THIS LINE
    
#=============================================


















##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################






__________ = False
___________ = 0

    
