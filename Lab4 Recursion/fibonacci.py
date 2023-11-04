"""
Lab 4 Exercise 3: The Fibonacci Sequence
Author: Bakhbyergyen Yerjan
Last Modified: 10/5/2022 1:29 PM
"""
# Recursion
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# Main function
def main():
    while True:
        try:
            [mode, num] = input("Enter mode and value:").split()
            num = int(num)
            assert num >= 0
        except ValueError:
            print('Invalid input. For mode either enter ''-i'' or ''-v.'' For value, please enter an integer greater than or equal to zero. Separate the two with a space.')
        except AssertionError:
            print('The number you entered should be 0 or greater.')
        else:
            break
    if mode == '-i':
        print(fibonacci(num))
    elif mode == '-v':
        i = 0
        res = fibonacci(i)
        while res < num:
            i += 1
            res = fibonacci(i)
        if res == num:
            print(f'{num} is in the sequence')
        else:
            print(f'{num} is not in the sequence')
    else:
        print('Check your mode. It needs to be either -i or -v')
main()