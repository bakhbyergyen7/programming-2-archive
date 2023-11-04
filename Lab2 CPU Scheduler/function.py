#function.py
class Function:
    def __init__(self, name, flag):
        self.name = name
        if flag == "yes":
            self.flag = True
        else:
            self.flag = False