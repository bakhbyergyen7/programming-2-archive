"""
Lab 5 : Beware of the Blob!
Author: Bakhbyergyen Yerjan
Last Modified: 10/17/2022 1:00 PM
"""

from blob import Blob

def main():
    file_name = input("Enter the name of the input file: ")
    blb = Blob(file_name)
    blb.run()

main()