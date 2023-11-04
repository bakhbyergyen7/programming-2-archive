# candy.py
# Sketch of Candy class

class Candy:
    def __init__(self, name):
        self.name = name
        self.rating =
        self.ingredients = []

    #magic methods to overload
    def __lt__(self, other):
        # if other is a Candy then
        # compare their names
        # if other is a string then
        # compare self.name to string
    def __eq__(self, other):

    def __gt__(self, other):

def main():
    candy1 = Candy('reeces cup')
    candy2 = Candy('starbursts')

    # if we define our magic correctly both of these comparisons
    # should be valid
    if candy1 < candy2: # campares two Candies
        # do something

    if candy1 < 'bit-o-honey': # comaring candy to string
        