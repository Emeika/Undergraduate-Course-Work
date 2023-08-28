# ===================================
# ===================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section: C
# Date   : 19/01/2023
# ===================================
# ===================================

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.visited = False

class Graph:
    def __init__(self):
        self.vertex = []

    def add_person(self, person):
        for vertex in self.vertex:
            if vertex.data == person:
                print('User already added')
                return
        vnode = Node(person)
        self.vertex.append(vnode)

    def add_friendship(self, person1, person2):
        person1_node = None
        person2_node = None
        for vertex in self.vertex:
            if vertex.data == person1:
                person1_node = vertex
            if  vertex.data == person2:
                person2_node = vertex
        if person1_node and person2_node:
            person1_node.next = Node(person2,person1_node.next)
            person2_node.next = Node(person1,person2_node.next)
        else:
            if person1_node is None:
                print("Person 1 do not exist in the graph.")
            elif person2_node is None:
                print("Person 2 do not exist in the graph.")

    def remove(self, person):
        person_node = None
        for vertex in self.vertex:
            if vertex.data == person:
                person_node = vertex
                break
        if person_node:
            self.vertex.remove(person_node)
            for v in self.vertex:
                current = v.next
                previous = v
                while current:
                    if current.data == person_node.data:
                        previous.next = current.next
                        current.next , current =  None, None
                    else:
                        previous = current
                        current = current.next
            person_node.next , person_node = None, None
        else:
            print(f"{person} does not exist in the graph.")

    def DFS(self, start):
        stack = []
        for v in self.vertex:
            if v.data == start:
                start_vertex = v
                break
        else:
            print(f"{start} does not exist in the graph.")
            return

        stack.append(start_vertex)
        while stack:
            vertex = stack.pop()
            if not vertex.visited:
                vertex.visited = True
                print(vertex.data)
                temp = vertex.next
                while temp is not None:
                    stack.append(temp)
                    temp = temp.next

    def BFS(self, start):
        queue = []
        visited = []
        for v in self.vertex:
            if v.data == start:
                start_vertex = v
                break
        else:
            print(f"{start} does not exist in the graph.")
            return
        queue.append(start_vertex)
        visited.append(start_vertex.data)
        while queue:
            vertex = queue.pop(0)
            print(vertex.data)
            friend = vertex.next
            while friend is not None:
                if friend.data not in visited and friend not in queue:
                    visited.append(friend.data)
                    queue.append(friend)
                friend = friend.next
                for v in self.vertex:
                    if friend is not None and v.data == friend.data:
                        friend_of_friend = v.next
                        while friend_of_friend is not None:
                            if friend_of_friend.data not in visited and friend not in queue:
                                visited.append(friend_of_friend.data)
                                queue.append(friend_of_friend)
                            friend_of_friend = friend_of_friend.next


network = Graph()
network.add_person('user1')
network.add_person('user2')
network.add_person('user3')
network.add_person('user4')
network.add_person('user5')
network.add_person('user6')

network.add_friendship('user1','user2')
network.add_friendship('user1','user3')
network.add_friendship('user4','user3')
network.add_friendship('user2','user6')
network.add_friendship('user2','user6')
network.add_friendship('user6','user4')
#

network.DFS('user1')
print()
network.BFS('user1')

'''def main():
    network = Graph()
    print('Enter commands at the prompt')
    print()
    print(
        'add_person, add_friendship, remove, BFS, DFS')
    print('Enter your commands in the above format -')
    command = input()

    while command != 'quit':
        if command == 'add_person':
            person = input('Enter user name to be added to the network: ')
            network.add_person(person)
        elif command == 'add_friendship':
            user1 = input('Enter person1 name: ')
            user2 = input('Enter person1 name: ')
            network.add_friendship(user1, user2)
        elif command == 'remove':
            remove_user = input('Enter the person name to be deleted: ')
            network.remove(remove_user)
        elif command == 'DFS':
            search = input('Enter the person name: ')
            network.DFS(search)
        elif command == 'BFS':
            search = input('Enter the person name: ')
            network.BFS(search)
        else:
            print("Command is invalid")

        command = input()

if __name__ == '__main__':
    main()'''






'''
friendship = input(f'Friend of {person} (Enter "none" if no friend): ')
if friendship != 'none':
    edge_head = Node(friendship)
    edge = edge_head
    choice = input('Any more friends? (y/n)').lower()
    while choice == 'y':
        previous = edge
        friendship = input(f'Friend of {person} : ')
        edge = Node(friendship)
        previous.next = edge
        choice = input('Any more friends? (y/n)').lower()
    vnode.next = edge_head'''