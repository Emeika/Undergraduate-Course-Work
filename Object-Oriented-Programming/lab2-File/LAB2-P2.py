#1

File_Name = input('Enter the Name of File: ')
Opened_File = open(File_Name , 'r')

charcount = 0
linecount = 0
wordcount = 0

line = Opened_File.readline()
while line != '':
	if line != '\n':
		linecount += 1
		wordlist = line.split()
		for word in wordlist:
				wordcount += 1
				charcount += len(word)
	line = Opened_File.readline()
			

print('Character Count : ',charcount,'\n','No. of Lines excluding empty lines: ',linecount,'\n','Word Count:',wordcount)

Opened_File.close()

