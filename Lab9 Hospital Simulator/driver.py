"""
Lab 9 : Hospital Simulator
Author: Bakhbyergyen Yerjan
Last Modified: 11/20/2022 6:04 PM
"""

from pokedex import Pokedex

def main():
    file_name = input("Enter the name of the input file: ")
    dex = Pokedex(file_name)
    dex.run()

main()