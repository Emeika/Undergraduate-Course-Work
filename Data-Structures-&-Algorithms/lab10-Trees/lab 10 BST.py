class BstNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,key):
        newnode = BstNode(key)

        temp = self.root

        y = None

        while temp != None:

            y = temp
            if key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        if y == None:
            y = newnode
            self.root = y

        elif key < y.data:
            y.left = newnode


        else:
            y.right = newnode

        return y

    def delete(self, data):

        def find_minimum(node):
            current = node
            while (current.left is not None):
                current = current.left

            return current

        def deleteNode(node, data):
            if node is None:
                return node

            if data < node.data:
                node.left = deleteNode(node.left, data)
            elif (data > node.data):
                node.right = deleteNode(node.right, data)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp

                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = find_minimum(node.right)

                node.data = temp.data
                node.right = deleteNode(node.right, temp.data)

            return node

        deleteNode(self.root, data)

    def Search(self,key):
        temp = self.root
        if temp == None:
            print('No data.')
            return
        if key == temp.data:
            print('found.',temp.data)
            return

        temp = self.root

        while key != temp.data:

            if key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        print('Data found ',temp.data)
        return temp.data

    def postorder(self):
        temp = self.root
        def post(temp):
            if temp == None:
                return
            else:
                post(temp.left)
                post(temp.right)
                print(temp.data, '', end='')
        post(temp)
    def preorder(self):
        temp = self.root
        def pre(temp):
            if temp == None:
                return
            else:
                print(temp.data, '', end='')
                pre(temp.left)
                pre(temp.right)
        pre(temp)
    def inorder(self):
        temp = self.root

        def inor(temp):
            if temp == None:
                return
            else:
                inor(temp.left)
                print(temp.data, '', end='')
                inor(temp.right)

        inor(temp)

    def GetParent(self,key):
        temp = self.root
        slow = None

        if temp == None:
            return

        while temp.data != key:
            slow = temp

            if key < temp.data:

                temp = temp.left
            else:
                temp = temp.right
        return slow.data


    def height(self):
        def depth(node):
            if node is None:
                return 0

            else:
                left_depth = depth(node.left)
                right_depth = depth(node.right)

                if left_depth > right_depth:
                    return left_depth + 1
                else:
                    return right_depth + 1

        return depth(self.root)


tree = Bst()
tree.insert(6)
tree.insert(7)
tree.insert(9)
tree.insert(1)
tree.insert(5)
tree.insert(7)
tree.Search(5)
tree.inorder()
print()
tree.postorder()
print()
tree.preorder()
print()
print(tree.GetParent(7))
tree.delete(7)
print(tree.height())