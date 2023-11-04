"""
Lab 7 : Binary Search Tree (Phase 1)
Author: Bakhbyergyen Yerjan
Last Modified: 10/31/2022 10:19 AM
"""

from pokedex import Pokedex

def main():
    file_name = input("Enter the name of the input file: ")
    dex = Pokedex(file_name)
    dex.run()

main()