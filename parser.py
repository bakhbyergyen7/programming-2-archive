# parser
from stack import Stack

def parser(l:list):
    s = Stack()
    for i in l:
        if i == "(":
            s.push(i)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()
        
par = ['(', ')','(',')']
print(parser(par))