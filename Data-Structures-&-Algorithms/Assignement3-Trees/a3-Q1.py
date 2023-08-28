# ===================================
# ===================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section: C
# Date   : 08/01/2023
# ===================================
# ===================================

#  PROBLEM 1

class BstNode:
    def __init__(self, title, cast_linked, year, minutes, left=None, right=None):
        self.title = title
        self.cast_linked = cast_linked
        self.year = year
        self.minutes = minutes
        self.left = left
        self.right = right


class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MovieBst:
    def __init__(self):
        self.root = None

    def add_movie(self, title, year, minutes, actors=None):
        # set root cast
        if actors is None:
            actor = input('Enter Cast Actor names: ')
            c = input('Any more Actors? y/n: ').lower()

            newnode = LinkedNode(actor)
            head = newnode

            while c == 'y':
                previous = newnode
                actor = input('Enter Cast Actor name: ')
                newnode = LinkedNode(actor)
                previous.next = newnode
                c = input('Any more Actors? y/n: ').lower()
        else:
            newnode = LinkedNode(actors[0])
            head = newnode
            for actor in actors:
                previous = newnode
                newnode = LinkedNode(actor)
                previous.next = newnode

        bstnode = BstNode(title, head, year, minutes)

        temp = self.root
        slow = None
        while temp is not None:
            slow = temp
            if bstnode.title < temp.title:
                temp = temp.left
            else:
                temp = temp.right

        if slow is None:  # Tree is empty
            slow = bstnode
            self.root = slow

        elif bstnode.title < slow.title:
            slow.left = bstnode

        else:
            slow.right = bstnode

    def delete_movie(self, title):
        def find_minimum(node):
            current = node
            while current.left is not None:
                current = current.left

            return current

        def deleteNode(node, movie_title):
            if node is None:
                print('No Record')
                return node

            if movie_title < node.title:
                node.left = deleteNode(node.left, movie_title)
            elif movie_title > node.title:
                node.right = deleteNode(node.right, movie_title)
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

                node.title = temp.title
                node.right = deleteNode(node.right, temp.title)

            return node

        deleteNode(self.root, title)

    def add_actor(self, title, actor):

        def add_to_linkedlist(tempnode, cast):
            itr = tempnode.cast_linked
            while itr.next is not None:
                itr = itr.next
            itr.next = LinkedNode(cast)

        if self.root is None:
            print('No record')
            return
        else:
            temp = self.root
            if temp.title == title:
                add_to_linkedlist(temp, actor)
                return
            else:
                while temp.title != title:

                    if temp.right is None and temp.left is None:
                        print('Movie Not Found')
                        break
                    elif title < temp.title and temp.left is not None:
                        temp = temp.left
                    elif temp.right is not None:
                        temp = temp.right
                add_to_linkedlist(temp, actor)

    def find_movie(self, title):
        def display(current):
            print('Found')
            print('Movie:', current.title, ' Release year:', current.year, ' Duration:', current.minutes)
            print('Cast: ', end='')
            itr = current.cast_linked
            while itr is not None:
                print(itr.data, ' ', end='')
                itr = itr.next

        if self.root is None:
            print('No Record')
            return
        else:
            temp = self.root
            if temp.title == title:
                display(temp)
            else:
                while temp.title != title:
                    if temp.right is None and temp.left is None:
                        print('Not Found')
                        break
                    elif title < temp.title and temp.left is not None:
                        temp = temp.left
                        if temp.title == title:
                            display(temp)
                    elif temp.right is not None:
                        temp = temp.right
                        if temp.title == title:
                            display(temp)

    def find_actor(self, actor):
        movies = []

        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            curr_node = root.cast_linked
            while curr_node is not None:
                if curr_node.data == actor:
                    movies.append(root.title)
                curr_node = curr_node.next

        postorder(self.root)
        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movie found for this actor.")

    def print_movies(self):
        def inorder(root):
            if root is None:
                return
            else:
                inorder(root.left)
                print(root.title, '', root.year, '', root.minutes, '', end='')
                itr = root.cast_linked
                while itr is not None:
                    print(itr.data, '', end='')
                    itr = itr.next
                print()
                inorder(root.right)

        inorder(self.root)

    def getHeight(self, root):
        if root is None:
            return -1
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def IsBSTBalanced(self):
        def isBSTBalanced(root):
            if root is None:
                return True
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)

            if abs(leftHeight - rightHeight) <= 1 and isBSTBalanced(root.left) and isBSTBalanced(root.right):
                return True
            else:
                return False

        return isBSTBalanced(self.root)

    def BalanceTree(self):
        def _BalanceTree(root):
            if not root:
                return root
            root.left = _BalanceTree(root.left)
            root.right = _BalanceTree(root.right)

            balance = getBalance(root)

            if balance > 1 and getBalance(root.left) >= 0:
                return rightRotate(root)

            if balance < -1 and getBalance(root.right) <= 0:
                return leftRotate(root)

            if balance > 1 and getBalance(root.left) < 0:
                root.left = leftRotate(root.left)
                return rightRotate(root)

            if balance < -1 and getBalance(root.right) > 0:
                root.right = rightRotate(root.right)
                return leftRotate(root)

            return root

        def getBalance(root):
            if not root:
                return 0
            return self.getHeight(root.left) - self.getHeight(root.right)

        def leftRotate(z):
            y = z.right
            T2 = y.left

            y.left = z
            z.right = T2

            return y

        def rightRotate(z):
            y = z.left
            T3 = y.right

            y.right = z
            z.left = T3

            return y

        return _BalanceTree(self.root)

    def InsertMovie_Balanced(self, title, year, minutes):
        self.add_movie(title, year, minutes)
        if not self.IsBSTBalanced():
            self.BalanceTree()

    def DeleteMovie_Balanced(self, title):
        self.delete_movie(title)
        if not self.IsBSTBalanced():
            self.BalanceTree()

    def save(self, fileName):
        outfile = open(fileName + '.txt', 'a+')

        def traverse(node):
            if node is None:
                return
            actors = []
            current = node.cast_linked
            while current is not None:
                actors.append(current.data)
                current = current.next
            print(node.title + ',' + str(node.year) + ',' + str(node.minutes) + ',' + ','.join(actors) + '\n', file=outfile, end='')
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        outfile.close()

    def load(self, filename):

        infile = open(filename + '.txt', 'r')
        for line in infile:
            line = line.strip().split(',')
            title = line[0]
            year = int(line[1])
            minutes = int(line[2])
            actors = line[3:]
            self.add_movie(title, year, minutes, actors)


def main():
    movieobj = MovieBst()
    print('Enter commands at the prompt')
    print()
    print('add_movie, delete_movie, add_actor, find_movie, find_actor, print_movies, IsBSTBalanced, BalanceTree\n '
          'InsertMovie_Balanced, DeleteMovie_Balanced, save, load')
    print('Enter your commands in the above format -')
    command = input()

    while command != 'quit':
        if command == 'add_movie':
            title = input('Enter Movie Title: ')
            year = int(input('Enter Movie year of release: '))
            minutes = int(input('Enter duration minutes: '))
            movieobj.add_movie(title, year, minutes)

        elif command == 'delete_movie':
            title = input('Enter the movie title to be deleted: ')
            movieobj.delete_movie(title)
        elif command == 'add_actor':
            title = input('Movie Name for which actor to be added: ')
            actor = input('Enter the Actor name: ')
            movieobj.add_actor(title, actor)
        elif command == 'find_movie':
            title = input('Movie Name to be found: ')
            movieobj.find_movie(title)
        elif command == 'find_actor':
            actor = input('Actor Name to be found in movies: ')
            movieobj.find_actor(actor)

        elif command == 'print_movies':
            movieobj.print_movies()
        elif command == 'IsBSTBalanced':
            if movieobj.IsBSTBalanced():
                print('True')
            else:
                print('False')
        elif command == 'BalanceTree':
            movieobj.BalanceTree()
        elif command == 'InsertMovie_Balanced':
            title = input('Enter Movie Title: ')
            year = int(input('Enter Movie year of release: '))
            minutes = int(input('Enter duration minutes: '))
            movieobj.InsertMovie_Balanced(title, year, minutes)
        elif command == 'DeleteMovie_Balanced':
            title = input('Enter the movie title to be deleted: ')
            movieobj.DeleteMovie_Balanced(title)
        elif command == 'save':
            file = input('Enter file name: ')
            movieobj.save(file)
        elif command == 'load':
            file = input('Enter file name: ')
            movieobj.load(file)
        else:
            print("Command is invalid")

        command = input()


if __name__ == '__main__':
    main()
