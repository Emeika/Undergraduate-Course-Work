# Task 2

input_str = 'HELLO World'
encstr = ''

for s in input_str:
    if (ord(s)) >= 65 and (ord(s) <= 90):
        encrypt = ord(s)+3
        encstr = encstr + encstr.join(chr(encrypt))
    elif s == ' ':
        encstr = encstr + encstr.join(' ')
    elif (ord(s)) >= 97 and (ord(s) <= 122):
        encrypt = ord(s)+3
        encstr = encstr + encstr.join(chr(encrypt))
print(encstr)

