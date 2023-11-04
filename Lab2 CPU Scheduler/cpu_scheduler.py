#cpu_scheduler.py

from process import Process
from linked_queue import Queue

class CPU_Scheduler:
    def __init__(self,file_name):
        self.processes = Queue()
        self.file_name = file_name
        self.command_list = []
        file = open(self.file_name,'r')
        for line in file:
            # command: ['command', 'name', 'opt:flag']
            command = line.replace('\n','').split()
            self.command_list.append(command)
        file.close()

    def start(self, process):
        self.processes.enqueue(Process(process))
        print(f"{process} added to the queue")

    def call(self, func, flg):
        try:
            front = self.processes.dequeue()
            front.call(func, flg)
            self.processes.enqueue(front)
            print(f"{front.id} called {func}")
        except:
            print("Can't dequeue. Make sure your queue is not empty.")

    def rtrn(self):
        try:
            proc = self.processes.dequeue()
            func_name = proc.rtrn()
            print(f"{proc.id} returns from {func_name}")
            if func_name != 'main':
                self.processes.enqueue(proc)
            else:
                print(f'{proc.id} process has ended.')
        except Exception as e:
            print("Try something valid!")
            print(e)

    def rse(self):
        proc = self.processes.peek()
        func_name = proc.rse()
        if func_name == 'main':
            self.processes.dequeue()
            print(f'{self.id} ended due to unhandled exception')
        else:
            print(f'{proc.id} has exception handled by {func_name}')


    def run(self):
        for command in self.command_list:
            if command[0] == "START":
                self.start(command[1])
            elif command[0] == "CALL":
                self.call(command[1], command[2])
            elif command[0] == "RETURN":
                # return - rtrn
                self.rtrn()
            elif command[0] == "RAISE":
                # raise - rse
                self.rse()