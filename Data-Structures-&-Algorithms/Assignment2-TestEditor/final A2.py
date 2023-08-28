# ===================================
# ===================================
# Name   : Hafsah Shahbaz
# Roll no: 251684784
# Section: C
# Date   : 4/12/2022
# ===================================
# ===================================


# ------------------------------------
# Node class for a Doubly Linked List
# ------------------------------------

import copy

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# ------------------------------------

class TextEditor:
    def __init__(self):
        '''
        Predefined member variables.

        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''

        self.doc = None  # The root of everything. See page 2 for details
        self.head = Node(self.doc)
        self.cursor = [-1, -1]
        self.row = -1
        self.col = -1

        self.stack = []
        self.redo_stack = []

        # ======================
        # Insert your Member
        #   variables here (if any):
        # ----------------------

        # ======================

    # ======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the
          row and col parameters

        Parameters:
            row --> row number to move to
            col --> column number to move to

        Return value:
            None
        '''
        green = self.head
        pink = self.head.data

        # Checks if the row/column number is negative or not
        if row >= 0 and col >= 0:
            for r in range(row):
                if green.next == None:  # Create an empty row nodes if cursor to any row does not exist
                    prev = green
                    n1 = Node(None, prev)
                    prev = n1
                    green.next = n1
                    green = green.next
                else:  # Iterate on already created to row to reach to the cursor
                    green = green.next
                    if green.data is not None:
                        pink = green.data

            if col == 0:
                cl = 1  # To iterate on 0
            else:
                cl = col

            # Create an empty column nodes if cursor to any col does not exist
            if green.data == None:

                previ = green
                pinkhead = Node(' ', previ)
                previ = pinkhead
                green.data = pinkhead
                if col == 0:
                    pass
                else:  # Cursor call to more than 0th pink/col node to create empty pink nodes/col
                    temp = pinkhead
                    for c in range(cl):
                        n2 = Node(' ', previ)
                        previ = n2
                        temp.next = n2
                        temp = temp.next

                pink = green.data

            # Iterate on col to reach to the cursor

            for c in range(col):
                if pink.next == None:  # append empty nodes after a currently existing line.
                    prev = pink
                    n1 = Node(' ', prev)
                    prev = n1
                    pink.next = n1

                pink = pink.next

            self.cursor = [row, col]  # Setting the cursor to current row and col

            # Setting at the character sitting at row/ column
            self.row = green
            self.col = pink

        else:  # Ignore negative values
            pass

        if len(self.stack) == 0 or self.head != self.stack[-1]:
            self.stack.append(copy.deepcopy(self.head))
        else:
            self.stack.append(copy.deepcopy(self.head))


    # ======================

    # ======================
    def forward(self):
        '''
        Moves the cursor one step forward

        Parameters:
            None

        Return value:
            None
        '''
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):
            col_temp = self.col
            if col_temp.next == None:
                row_temp = self.row
                # row_temp.next == None then it's the end of document( no change to cursor)
                if row_temp.next is not None and row_temp.next.data is not None:  # Not the end of the document

                    # cursor is at last character of the current line
                    # then forwarding it will move it to the first character of the next line.
                    row_temp = row_temp.next
                    self.cursor[0] += 1

                    col_temp = row_temp.data  # the next line isn't empty
                    self.row, self.col = row_temp, col_temp
                    self.cursor[1] = 0

            else:
                self.col = self.col.next
                self.cursor[1] += 1


    # ======================

    # ======================
    def back(self):
        '''
        Moves the cursor one step backwards

        Parameters:
            None

        Return value:
            None
        '''
        # operation on an invalid cursor shall be ignored
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):
            col_temp = self.col
            if col_temp.prev == self.row:
                row_temp = self.row
                # row_temp.prev == None then it's the begining of document( no change to cursor)

                if row_temp.prev is not None and row_temp.prev.data is not None:
                    row_temp = row_temp.prev
                    self.cursor[0] -= 1

                    # cursor is at first character of the current line
                    # then backing it will move it to the last character of the previous line.

                    col_temp = row_temp.data  # the prev line isn't empty
                    pink_count = 0  # Total Pink Node to set the cursor to the end of the line
                    while col_temp.next is not None:  # Last pink node
                        col_temp = col_temp.next
                        pink_count += 1
                    self.row, self.col = row_temp, col_temp
                    self.cursor[1] = pink_count
            else:
                self.col = self.col.prev
                self.cursor[1] -= 1


    # ======================

    # ======================
    def home(self):
        '''
        Moves the cursor to the start of the current line

        Parameters:
            None

        Return value:
            None
        '''
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):
            self.cursor = [0, 0]
            self.row = self.head
            self.col = self.head.data


    # ======================

    # ======================
    def end(self):
        '''
        Moves the cursor to the end of the current line

        Parameters:
            None

        Return value:
            None
        '''
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):
            temp = self.head
            green_count = 0
            # Iterates till the last row and count the number of rows
            while temp.next is not None:
                temp = temp.next
                green_count += 1

            self.col = temp.data
            pink_count = 0
            # Iterates till the last col ad count the number of cols
            while self.col.next is not None:
                self.col = self.col.next
                pink_count += 1
            self.cursor = [green_count, pink_count]
            self.row = temp

    # ======================

    # ======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor

        Parameters:
            a string

        Return value:
            None
        '''
        if len(self.stack) == 0 or self.head != self.stack[-1]: # condition to make sure same values of sheet are not pushed to stack
            # insert deepcopy of sheet into stack before any insertion
            self.stack.append(copy.deepcopy(self.head))


        str_len = len(string)
        chr_list = []
        for char in string:
            chr_list.append(char)

        if self.cursor == [-1, -1]:
            green = self.head
            prev = green
            node = Node(chr_list[0], prev)
            prev = node
            green.data = node

            for i in range(str_len - 1):
                node.next = Node(chr_list[i + 1], prev)
                node = node.next
                prev = node
            self.cursor = [0, str_len - 1]
            self.row = self.head
            self.col = self.row.data
            for x in range(str_len - 1):
                self.col = self.col.next

        else:
            def _insert_between(e, predecessor, successor):
                newest = Node(e, predecessor, successor)
                predecessor.next = newest
                if successor is not None:
                    successor.prev = newest
                return newest

            if self.col.next is not None:  # insert in between
                for i in range(str_len):
                    self.col = _insert_between(chr_list[i], self.col, self.col.next)
                self.cursor[1] += str_len

            if self.row.data.next == None:  # insert first when empty
                self.col.data = chr_list[0]
                for i in range(str_len-1):
                    self.col = _insert_between(chr_list[i+1], self.col, self.col.next)
                self.cursor[1] += str_len - 1

            else:
                if self.col.next == None:  # insert Last
                    for i in range(str_len):
                        self.col = _insert_between(chr_list[i], self.col, self.col.next)

                self.cursor[1] += str_len

        self.stack.append(copy.deepcopy(self.head))

    # ======================

    # ======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position

        Parameters:
            integer number of characters to delete

        Return value:
            None
        '''
        if len(self.stack) == 0 or self.head != self.stack[-1]:
            self.stack.append(copy.deepcopy(self.head))
        if num > 0 and (self.cursor is not [-1, -1]) and (self.col and self.row != -1):

            def _delete_node(node):
                predecessor = node.prev
                successor = node.next
                if predecessor != self.row:
                    predecessor.next = successor
                else:
                    predecessor.data = successor
                if successor != None:
                    successor.prev = predecessor
                if node.next is not None:
                    current = node.next
                else:
                    current = node.prev
                node.prev = node.next = node.data = None
                return current

            temp = self.col

            count = 0  # Total nodes after the cursor
            while temp is not None:
                temp = temp.next
                count += 1
            # special case 3
            if self.cursor[1] == 0 and count <= num:  # Deleting entire line
                for n in range(count):
                    self.col = _delete_node(self.col)

                # cursor will point to the first character of the next line.
                if self.row.next != None and self.row.next.data != None:
                    self.cursor[0] = self.cursor[0] + 1
                    self.row = self.row.next
                    self.col = self.row.data
                elif self.row.next == None:  # end of the document, creates empty next line
                    self.row.next = Node(None, self.row)
                    self.row.next.data = Node(' ', self.row.next)
                    self.cursor[0] = self.cursor[0] + 1
                    self.row = self.row.next
                    self.col = self.row.data
                elif self.row.next.data == None and self.row.next != None:  # Next line is empty
                    self.row.next.data = Node(' ', self.row.next)
                    self.cursor[0] = self.cursor[0] + 1
                    self.row = self.row.next
                    self.col = self.row.data

            # Special case 2
            else:
                if count <= num:  # Num of nodes to be deleted id greater than the actual nodes
                    for n in range(count):
                        self.col = _delete_node(self.col)
                    # cursor will point to the immediately previous character
                    self.cursor[1] = self.cursor[1] - 1
                elif count > num:
                    # General case - Cursor position doesn't change
                    for n in range(num):
                        self.col = _delete_node(self.col)

            self.stack.append(copy.deepcopy(self.head))

    # ======================
    def countCharacters(self):
        '''
        Moves the cursor to the start of the current line

        Parameters:
            None

        Return value:
            total number of characters in the document, basically
               the total number of pink nodes in the document.
        '''

        greentemp = self.head
        char_count = 0
        while greentemp is not None:
            if greentemp.data is not None:
                pinktemp = greentemp.data
                while pinktemp is not None:
                    char_count += 1
                    pinktemp = pinktemp.next

            greentemp = greentemp.next
        return char_count

    # ======================

    # ======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.

        Parameters:
            None

        Return value:
            integer number of non-empty lines in the document
        '''
        greentemp = self.head
        line_count = 0
        while greentemp is not None:
            if greentemp.data is not None:
                line_count += 1
            greentemp = greentemp.next

        return line_count

    # ======================

    # ======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''

        green = self.head
        col_count = 0
        row_count = 0
        while green is not None:
            pink = green.data
            if pink is not None:
                while pink is not None:
                    if self.cursor[1] == col_count and self.cursor[0] == row_count:
                        print('|', end='')
                    print(pink.data, end='')
                    pink = pink.next
                    if self.cursor[0] == row_count:
                        col_count += 1
            green = green.next
            print('\n', end='')
            row_count += 1


    # ======================

    # ======================
    # ======================
    #    BONUS
    # ======================
    def undo(self):
        '''
        Undos the previous action by user.

        Parameters:
            None

        Return value:
            None

        '''
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):
            self.redo_stack.append(self.stack.pop())
            self.head = self.stack[-1]
            # pops from the undo stack and pushes into the redo stack

    # ----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.

        Parameters:
            None

        Return value:
            None

        '''
        if (self.cursor is not [-1, -1]) and (self.col and self.row != -1):

            self.stack.append(self.redo_stack.pop())
            self.head = self.stack[-1]

    # ----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter

        Parameters:
            fileName

        Return value:
            None

        '''

        outfile = open(fileName + '.txt', 'a+')

        # prints row by row with all its columns inside
        green = self.head
        col_count = 0
        row_count = 0
        while green is not None:
            pink = green.data
            if pink is not None:
                while pink is not None:
                    if self.cursor[1] == col_count and self.cursor[0] == row_count:
                        print('|', file=outfile, end='')
                    print(pink.data, file=outfile, end='')
                    pink = pink.next
                    if self.cursor[0] == row_count:
                        col_count += 1

            green = green.next
            print('\n', file=outfile, end='')
            row_count += 1

        outfile.close()

    # ----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter

        Parameters:
            fileName

        Return value:
            None

        '''

        infile = open(fileName + '.txt', 'r')
        temp = self.head

        x = infile.read().split('\n')

        for count, line in enumerate(x,1):

            if line.rstrip() != '':
                if line == x[-1]:
                    self.goto(count-1, 0)
                    self.insert(line.rstrip())
                else:
                    self.goto(count-1, 0)  # used for the else condition
                    self.insert(line.rstrip())

                    self.goto(count,0) # moves to the next line row after inserting

            else:
                 # Create an empty row nodes if cursor to any row does not exist
                temp.next = Node(None, temp)
            temp = temp.next

        infile.close()

    # ----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.

        Parameters:
            substring to look for

        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''

        # Don't search if self.doc is None.
        if (self.cursor is [-1, -1]) and (self.col and self.row == -1):
            return

        # Only search if it is possible for the substring to be in the document.
        if self.countCharacters() >= len(substr):

            # Traversing through the document.
            green = self.head

            while green is not None:
                try:
                    if green.data is not None:
                        pink = green.data
                        while pink is not None:
                            if pink.data == substr[0]:
                                found_flag = True
                                substring_temp = pink

                                for i in range(len(substr)):
                                    if substring_temp.data == substr[i]:
                                        substring_temp = substring_temp.next

                                    else:
                                        found_flag = False

                                if found_flag is True:
                                    #print('found ', substr,'at ',pink)
                                    return f"{substr} found at {pink} onwards."

                            pink = pink.next
                except:
                    return None

                green = green.next

        return None


# ======================

# ======================
# ======================
#
#    DRIVER FUNCTION
#
# ======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    editor = TextEditor()
    print('Welcome to DS Text Editor\nEnter commands at the prompt: ')
    command = input()

    while command != 'quit':
        if command[:6] != 'insert':
            command = command.lower().split()

        if command[0] == 'goto':
            editor.goto(int(command[1]), int(command[2]))
        elif command[0] == 'forward':
            editor.forward()
        elif command[0] == 'back':
            editor.back()
        elif command[0] == 'home':
            editor.home()
        elif command[0] == 'end':
            editor.end()
        elif command[:6] == 'insert':
            editor.insert(command[7:])
        elif command[0] == 'delete':
            editor.delete(int(command[1]))
        elif command[0] == 'countcharacters':
            print(editor.countCharacters())
        elif command[0] == 'countlines':
            print(editor.countLines())
        elif command[0] == 'printdoc':
            editor.printDoc()
        elif command[0] == 'save':
            editor.save(command[1])
        elif command[0] == 'load':
            editor.load(command[1])
        elif command[0] == 'find':
            print(editor.find(command[1]))
        elif command[0] == 'undo':
            editor.undo()
        elif command[0] == 'redo':
            editor.redo()
        else:
            print("Command is invalid")

        command = input()


if __name__ == '__main__':
    main()