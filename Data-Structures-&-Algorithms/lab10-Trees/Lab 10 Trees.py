# Hafsah Shahbaz
# 251684784

# Task 1
class Node:
    def __init__(self,data,parent=None,left=None,right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def AddLeft(self,node,data):
        node.left = Node(data,node)
        self.size += 1

    def GetLeft(self,node):
        return node.left

    def AddRight(self,node,data):
        node.right = Node(data,node)
        self.size += 1

    def GetRight(self,node):
        return node.right

    def SetRoot(self, data):
        self.root = Node(data)

    def GetRoot(self):
        return self.root

    def is_Leaf(self, node):
        if node.right and node.left == None:
            return True
        else:
            return False

    def GetParent(self, node):
        return node.parent

    def __len__(self):
        return self.size


# Task 2
T = BinaryTree()
T.SetRoot(11)

root = T.GetRoot()
T.AddLeft(root, 6)
T.AddRight(root, 19)

temp_node = T.GetLeft(root)
T.AddLeft(temp_node, 4)
T.AddRight(temp_node, 8)

temp_node = T.GetLeft(temp_node)
T.AddRight(temp_node, 5)

temp_node = temp_node.parent
T.AddRight(temp_node, 8)

temp_node = T.GetRight(temp_node)
T.AddRight(temp_node, 10)

temp_node = T.GetRoot()
temp_node = T.GetRight(temp_node)
T.AddLeft(temp_node, 17)
T.AddRight(temp_node, 43)

temp_node = T.GetRight(temp_node)
T.AddLeft(temp_node, 31)
T.AddRight(temp_node, 49)
# Task 3

def postorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data,'', end ='')

def preorder(root):
    if root == None:
        return
    else:
        print(root.data,'', end ='')
        postorder(root.left)
        postorder(root.right)

def inorder(root):
    if root == None:
        return
    else:
        postorder(root.left)
        print(root.data,'', end ='')
        postorder(root.right)



def bfs(root):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node.data,'', end ='')

        if cur_node.left is not None:
            queue.append(cur_node.left)


        if cur_node.right is not None:
            queue.append(cur_node.right)

print("Pre-order:", end=" ")
preorder(T.GetRoot())
print()

print("In-order:", end=" ")
inorder(T.GetRoot())
print()

print("Post-order:", end=" ")
postorder(T.GetRoot())
print()


print("BFS:", end=" ")
bfs(T.GetRoot())