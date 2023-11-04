#Author: Bakhbyergyen Yerjan | Date Modified: 9/28/2022 2:43 PM
from browser import Browser

def main():
    file_name = input("Enter the name of the input file: ")
    brwsr = Browser(file_name)
    brwsr.run()

main()