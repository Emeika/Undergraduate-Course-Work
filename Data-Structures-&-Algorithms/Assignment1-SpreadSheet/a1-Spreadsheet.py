# ===================================
# ===================================
# Name   : Hafsah Shabaz
# Roll no: 251684784
# Section: C
# Date   : 06/11/2022
# ===================================
# ===================================

class Spreadsheet:
    def __init__(self):
        """
        Predefined member variables.

        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        """
        self.sheet = None   # 2D array of values
        self.rows = 0
        self.cols = 0
        self.cursor = [0, 0]   # cursor's current position
        self.selction = [None, None, None, None]

        # ======================
        # Insert your Member
        #   variables here (if any):
        # ----------------------
        self.value = []   # List of values inside the selection

        # ======================

# ======================
    def CreateSheet(self, rows, cols):
        """
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.

        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet

        Return value:
            None
        """
        sheetlist = []
        for r in range(rows):
            col = []
            for c in range(cols):
                col.append(None)
            sheetlist.append(col)        # appends the complete line of a single row

        # Sets the values
        self.sheet = sheetlist
        self.rows = rows
        self.cols = cols


# ======================


# ======================

    def Goto(self, row, col):
        """
        Moves the cursor to the location indicated by the
          row and col parameters

        Parameters:
            row --> row number to move to
            col --> column number to move to

        Return value:
            None
        """
        self.cursor = [row, col]


# ======================

# ======================

    def Insert(self, val):
        """
        Inserts value at the position indicated by the cursor.

        Parameters:
            val --> value to be inserted at the cursor location

        Return value:
            None
        """
        self.sheet[self.cursor[0]][self.cursor[1]] = val

# ======================

# ======================
    def Delete(self):
        """
        Deletes a value from the position indicated by the cursor.

        Parameters:
            #none

        Return value:
            None
        """
        self.sheet[self.cursor[0]][self.cursor[1]] = None


# ======================

# ======================

    def ReadVal(self):
        """
        Prints the value from the position indicated by the cursor.

        Parameters:
            #None

        Return value:
            value stored at the cursor location

        """

        print(self.sheet[self.cursor[0]][self.cursor[1]])
# ======================

# ======================
    def Select(self, row, col):
        """
        Selects values between the position indicated in arguments with row and col
        and the position indicated by the cursor

        Parameters:
            row --> Row number to be selected
            col --> Column number to be selected

        Return value:
            None
        """

        self.selction = [self.cursor[0], self.cursor[1], row, col]

        ur = self.selction[0]  # upper left corner row
        lr = self.selction[2]  # lower right corner row

        uc = self.selction[1]  # upper left corner column
        lc = self.selction[3]  # lower right corner column

        values = []
        if ur < lr:
            for r in range(ur, lr+1):
                values.append(self.sheet[r][uc])
                if uc < lc:
                    for c in range(uc, lc):
                        values.append(self.sheet[r][c + 1])  # Appends the values in the column till the selection
                else:
                    for c in range(lc, uc):  # for reverse selection of values
                        values.append(self.sheet[r][c])
        else:
            for r in range(lr, ur+1):
                values.append(self.sheet[r][uc])
                if uc < lc:
                    for c in range(uc, lc):
                        values.append(self.sheet[r][c + 1])  # Appends the values in the column till the selection
                else:
                    for c in range(lc, uc):  # for reverse selection of values
                        values.append(self.sheet[r][c])

        self.value = values


# ======================

# ======================

    def GetSelection(self):
        """
        Returns a tuple with current selecion cooridnates
        Parameters:
            #None

        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection

            Example: (1,1,3,4)
        """

        print(tuple(self.selction))

# ======================

# ======================
    def Sum(self, row, col):
        """
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum

        Return value:
            None
        """
        total = 0
        if self.value:
            for val in self.value:
                if val is not None:
                    total += val
        else:              # If there is no valid selection then use only one cell of cursor.
            if self.sheet[self.cursor[0]][self.cursor[1]] is not None:
                total = self.sheet[self.cursor[0]][self.cursor[1]]   # Sum is the value of current cursor location

        # if current cursor value is empty then Sum is zero
        self.sheet[row][col] = total


# ======================

# ======================

    def Mul(self, row, col):
        """
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product

        Return value:
            None
        """
        multiply = 1
        if self.value:
            for val in self.value:
                if val is not None:
                    multiply *= val
        else:                # If there is no valid selection then use only one cell of cursor.
            if self.sheet[self.cursor[0]][self.cursor[1]] is not None:
                multiply = self.sheet[self.cursor[0]][self.cursor[1]]   # Mul is the value of current cursor location
            else:
                multiply = 0    # if current cursor value is empty then mul is zero

        self.sheet[row][col] = multiply


# ======================

# ======================

    def Avg(self, row, col):
        """
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average

        Return value:
            None
        """

        total = 0
        count = 0
        if self.value:
            for val in self.value:
                if val is not None:
                    total += val
                    count += 1
            avg = round((total / count), 2)
        else:            # If there is no valid selection then use only one cell of cursor.
            if self.sheet[self.cursor[0]][self.cursor[1]] is not None:
                avg = self.sheet[self.cursor[0]][self.cursor[1]]   # Avg is the value of the current cursor location
            else:
                avg = 0             # if current cursor value is empty then Avg is zero

        self.sheet[row][col] = avg

# ======================

# ======================
    def Max(self, row, col):
        """
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum

        Return value:
            None
        """

        maximum = 0
        temp = []     # to get a list of values removing the None for max function
        if self.value:
            for val in self.value:
                if val is not None:
                    temp.append(val)
            maximum = max(temp)

        else:
            if self.sheet[self.cursor[0]][self.cursor[1]] is not None:
                maximum = self.sheet[self.cursor[0]][self.cursor[1]]

        self.sheet[row][col] = maximum

# ======================

# ======================
    def PrintSheet(self):
        """
        Prints the sheet in a human-readable from
        Parameters:
            #None
        Return value:
            None

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0
            1
            2           10
            3                   12
            4
        """

        space = '\t'  # stores the space tab

        # for printing the column heading
        print('row/col:', end='')
        for i in range(self.cols):
            print('   ', i, '\t', end='')
        print('\n', end='')

        for y in range(self.rows):       # printing of rows
            print(f'{y: 6d}', end='')
            for x in range(self.cols):   # printing of the values inside each column
                if self.sheet[y][x] is not None:
                    print(f'{self.sheet[y][x]: 7.2f} ', end='')   # Spaces are added so that the field width is 7

                else:                   # if list index is None then leave empty space
                    print(f'{space :6s} ', end='')

            print('\n', end='')
# ======================


# ======================
# ======================
#    BONUS
# ======================
    def Undo(self):
        """
        Undoes the previous action by user.

        Parameters:
            #None

        Return value:
            None

        """

        raise NotImplementedError


# ----------------------

    def Redo(self):
        """
        Redoes the previous action undone by user.

        Parameters:
            #None

        Return value:
            None

        """

        raise NotImplementedError

# ----------------------

    def Save(self, fileName):
        """
        Saves the spreadsheet to a file with name given as Parameter

        Parameters:
            fileName

        Return value:
            None

        """
        outfile = open(fileName + '.txt', 'a+')

        # prints row by row with all its columns inside
        for i in self.sheet:
            if i is not None:
                print(*i, file=outfile, sep=",")    # * unpacks from the list
            else:
                print('None', file=outfile, sep=",")

        outfile.close()


# ----------------------

    def Load(self, fileName):
        """
        Loads the spreadsheet from a file with name given as Parameter

        Parameters:
            fileName

        Return value:
            None

        """

        infile = open(fileName + '.txt', 'r')

        col_ct = len(infile.readline().strip().split(','))   # count the number of columns in a single line
        self.cols = col_ct

        #  read lines method read all lines in file and store in a list
        row_ct = len(infile.readlines())    # count the number of lines
        self.rows = row_ct

        infile.seek(0)  # reset a file read/write position

        split_list = []
        for line in infile:
            split_list.append(line.strip().split(','))   # appends the list of line into the split_list in string

        two_d = []

        for r in split_list:
            col = []
            for c in r:
                if c != 'None':
                    col.append(float(c))
                else:
                    col.append(None)
            two_d.append(col)

        self.sheet = two_d
        infile.close()

# ======================


# ======================
# ======================
#
#    DRIVER FUNCTION
#
# ======================

def main():

    print('Welcome to DS SpreadSheet Program.\nEnter commands at the prompt')
    print()
    print('[CreateSheet- row col] [Goto- row col] [Insert- data] [Delete] [ReadVal] [Select- row col]''\n'
          '[GetSelection] [Sum-	row col] [Mul- row col] [Avg- row col] [Max- row col] [PrintSheet]''\n'
          '[Quit] [Undo] [Redo] [Save- file name] [Load- file name]')
    print('Enter your commands in the above format -')

    sheet = Spreadsheet()
    command = input('\n')  # (CreateSheet 100 200) Take Command
    inp = command.split()
    quits = False
    while not quits:    # loop breaks when user enters quit

        ext = False
        while not ext:   # no other command before creating sheet

            if inp[0].lower() == 'createsheet':
                sheet.CreateSheet(int(inp[1]), int(inp[2]))
                print('Sheet successfully created !')
                ext = True

            elif inp[0].lower() == 'quit':
                ext = True
                quits = True

            elif inp[0].lower() == 'load':
                sheet.Load(inp[1])
                ext = True

            else:  # if you run any other command before creating a new sheet then it should display an error.
                print('Create a new sheet before running any other command:')
                command = input('\n')  # CreateSheet 100 200
                inp = command.split()  # list
        if not quits:
            user_inp = False
            while not user_inp:

                command = input('\n')  # CreateSheet 100 200
                inp = command.split()

                if inp[0].lower() == 'goto':
                    sheet.Goto(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'insert':
                    sheet.Insert(float(inp[1]))

                elif inp[0].lower() == 'delete':
                    sheet.Delete()

                elif inp[0].lower() == 'readval':
                    sheet.ReadVal()

                elif inp[0].lower() == 'select':
                    sheet.Select(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'getselection':
                    sheet.GetSelection()

                elif inp[0].lower() == 'sum':
                    sheet.Sum(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'mul':
                    sheet.Mul(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'avg':
                    sheet.Avg(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'max':
                    sheet.Max(int(inp[1]), int(inp[2]))

                elif inp[0].lower() == 'printsheet':
                    sheet.PrintSheet()

                elif inp[0].lower() == 'quit':
                    quits = True
                    user_inp = True

                elif inp[0].lower() == 'save':
                    sheet.Save(inp[1])

                elif inp[0].lower() == 'load':
                    sheet.Load(inp[1])

                else:
                    print('Invalid command. ')


if __name__ == '__main__':
    main()

# ======================
