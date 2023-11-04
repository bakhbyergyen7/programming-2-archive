# boardgame.py
class Boardgame:
    def __init__(self, name, GR, PR, year, MP, MT):
        self.name = name
        self.year = int(year)
        self.GR = float(GR)
        self.PR = float(PR)
        self.MP = int(MP)
        self.MT = int(MT)
    def __str__(self):
        return f"{self.name} ({self.year}) [GR={self.GR} PR={self.PR} MP={self.MP} MT={self.MT}]"
    def __lt__(self,other):
        return self.GR < other.GR
    def __gt__(self,other):
        return self.GR > other.GR