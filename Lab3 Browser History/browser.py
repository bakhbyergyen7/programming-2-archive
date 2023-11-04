#Author: Bakhbyergyen Yerjan | 9/26/2022 | Modified time 9:29PM

from linked_list import LinkedList

class Browser:
    def __init__(self, file_name):
        #Initialize Browser
        self.history = LinkedList()
        self.currpage = -1
        self.file_name = file_name
        self.command_list = []
        file = open(self.file_name,'r')
        for line in file:
            # command: ['command', 'URL']
            command = line.replace('\n','').split()
            self.command_list.append(command)
        file.close()

    def navigate_to(self,url):
        #The browser navigate to the given url
        while ((self.history.length()-1) != self.currpage):
            indx = self.history.length()-1
            self.history.remove(indx)
        self.history.insert(self.currpage+1,url)
        self.currpage += 1

    def forward(self):
        #If possible, the browser navigates forward in the history otherwise it keeps focus
        if self.currpage != self.history.length()-1 and self.history.length() >=1:
            self.currpage += 1
        else:
            self.currpage = self.history.length()-1

    def back(self):
        #If possible, the browser navigates backwards in the history otherwise it keeps focus
        if self.currpage!=0 and self.history.length()>=1:
            self.currpage -=1
        else:
            self.currpage = 0

    def history(self):
        #Returns a well formatted string (see below) with the current history.
        print('Oldest \n===========')
        try:
            for i in range(self.history.length()):
                if i == self.currpage:
                    print(f"{self.get_entry(self.currpage)} <==current")
                else:
                    print(f"{self.get_entry(i)}")
        except:
            print("No sites visited.")
        print('Newest\n ===========')

    def run(self):
        for command in self.command_list:
            if command[0] == "NAVIGATE":
                self.navigate_to(command[1])
            elif command[0] == "FORWARD":
                self.forward()
            elif command[0] == "BACK":
                self.back()
            elif command[0] == "HISTORY":
                self.history()
            else:
                print("Unknown commmand!")