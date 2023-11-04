"""
Lab 4 Exercise 1: Recursive Power Function
Author: Bakhbyergyen Yerjan
Last Modified: 10/2/2022 5:47 PM
"""

def raise_to_power(base,power):
    if power == 0:
        return 1
    else:
        return base * raise_to_power(base,power-1)

# Makes sure that we have a correct input for base

def main():
    while True:
        try:
            base = int(input("Enter a base:"))
        except ValueError:
            print("Not an integer! Enter an integer please.")
            continue
        else:
            break

    # Makes sure that we have a correct input for power
    while True:
        try:
            power = int(input("Enter a power:"))
            assert power >= 0
        except ValueError:
            print("Not an integer! Enter an integer please.")
            continue
        except AssertionError:
            print("Sorry, your exponent must be zero or larger.")
            continue
        else:
            break
    print(f"Answer: {raise_to_power(base,power)}")

main()