# process.py
from linked_stack import Stack
from function import Function
class Process:
    def __init__(self,id):
        self.id = id
        self.stack = Stack()
        self.stack.push(Function('main', 'no'))
    def call(self, fn, flg):
        return self.stack.push(Function(fn, flg))
    def rtrn(self):
        func = self.stack.pop()
        return func.name
    def rse(self):
        func = self.stack.pop()
        print(f'{self.id} encountered a raised exception by {func.name}')
        while not func.flag and func.name != 'main':
            func = self.stack.pop()
            print(f'{self.id} ends {func.name} due to unhandled exception')
        if func.flag:
            return func.name
        else:
            return 'main'
