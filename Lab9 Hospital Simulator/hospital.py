#Author: Bakhbyergyen Yerjan | 11/20/2022 | Modified time 6:29PM


class Hospital:
    def __init__(self, file_name):
        self.file_name = file_name
        self.command_list = []
        file = open(self.file_name,'r')
        for line in file:
            # command: ['command', 'URL']
            command = line.replace('\n','').split()
            self.command_list.append(command)
        file.close()


    def arrive(self):
        pass

    def count(self):
        pass

    def next(self):
        pass

    def treat(self):
        pass

    def run(self):
        for command in self.command_list:
            if command[0] == "ARRIVE":
                self.arrive()
            elif command[0] == "COUNT":
                self.count()
            elif command[0] == "NEXT":
                self.next()
            elif command[0] == "TREAT":
                self.treat()
            else:
                print("Unknown commmand!")