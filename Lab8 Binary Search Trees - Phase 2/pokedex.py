from binarysearchtree import BinarySearchTree
from pokemon import Pokemon

class Pokedex:
    def __init__(self, file_name):
        self.bst = BinarySearchTree()
        self.file_name = file_name
        self.file_reader()

    def file_reader(self):  
        file = open(self.file_name, 'r')
        for line in file:
            poke = line.strip().split()
            self.bst.add(Pokemon(''.join(poke[0:-2]), poke[-2], poke[-1]))
        file.close()

    def run(self):
    #         present options
            user_selection = 0
            while user_selection != 6:
                print(""" 
                1. Search by pokedox number \n 
                2. Add a new Pokemon \n 
                3. Print using in order \n 
                4. Print using pre order \n 
                5. Print using post order \n 
                6. Copy
                7. Remove
                8. Quit """)
                user_selection = input("Enter the number before the option you want: ")
                if user_selection == "1":
                    num = int(input("Enter the pokedox number you'd like to search: "))
                    try:
                        print(self.bst.search(num))
                    except:
                        raise Exception('A Pokemon with the given number does not exist')

                elif user_selection == "2":
                    new_US = input("Enter the US name:")
                    new_JP = input("Enter the JP name:")
                    new_id = input("Enter the pokedox number:")
                    new_pokemon = Pokemon(new_US, new_id, new_JP)
                    self.bst.add(new_pokemon)
                elif user_selection == "3":
                    self.bst.traverse_in()
                elif user_selection == "4":
                    self.bst.traverse_pre()
                elif user_selection == "5":
                    self.bst.traverse_post()
                elif user_selection == "6":
                    self.bst.copy()
                elif user_selection == "7":
                    target = input("Enter dex number to remove: ")
                    self.bst.remove(int(target))
                elif user_selection == "8":
                    print("We're quiting...")
                    exit()
                    
                else:
                    print("Invalid input. Please make sure your input is a number between 1 and 6")