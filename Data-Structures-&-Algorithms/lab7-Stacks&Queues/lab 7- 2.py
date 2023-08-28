# Question 2: [Weightage: 15%]
# Write a python program that checks brackets are balanced in an expression using stack.

from Stack import Stack

stackobj = Stack()


def check_balance(inp):

    for c in inp:
        if c in ['(', '{', '[']:
            stackobj.push(c)
        else:
            current = stackobj.pop()
            if current == '(' and c != ')':
                return False
            if current == '{' and c != '}':
                return False
            if current == '['and c != ']':
                return False
    if stackobj.is_empty():
        return True

def main():
    inp = input('Enter to check brackets: ')

    if check_balance(inp):
        print("Balanced")
    else:
        print("Not Balanced")

main()