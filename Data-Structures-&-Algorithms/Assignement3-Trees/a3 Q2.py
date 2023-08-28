# ===================================
# ===================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section: C
# Date   : 08/01/2023
# ===================================
# ===================================

#  PROBLEM 2


class Node:
    def __init__(self, data, left= None, right=None):
        self.data = data
        self.left = left
        self.right = right
class ExpTree:
    def __init__(self, root=None):
        self.root = root

    def parsePostfix(self, expression):
        node_stack = []  # Create a Stack
        for symbol in expression:
            if symbol.isnumeric() or symbol.isalpha():
                # create new expression tree with single node for value/variable
                val_node = Node(symbol)
                # push node to stack
                node_stack.append(val_node)
            else:
                # pop out two trees T1 and T2 from the stack
                t2 = node_stack.pop()
                t1 = node_stack.pop()
                # create new tree with operator as root and t1 and t2 as two children
                operator_node = Node(symbol, t1, t2)

                # push new tree to stack
                node_stack.append(operator_node)

        # at the end, the stack should contain a single tree
        self.root = node_stack.pop()

    def toInfix(self):

        def inorder(root):
            if root is None:
                return
            else:
                if root.data in ('+', '-', '*', '/'):
                    print('(', end='')
                inorder(root.left)
                print(root.data, end='')
                inorder(root.right)
                if root.data in ('+', '-', '*', '/'):
                    print(')', end='')

        inorder(self.root)



def main():
    expt = ExpTree()
    expt.parsePostfix("xx*2+x1+/")
    expt.toInfix()

main()