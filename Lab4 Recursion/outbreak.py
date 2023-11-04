"""
Lab 4 Exercise 2: Outbreak Returns
Author: Bakhbyergyen Yerjan
Last Modified: 10/3/2022 11:01 AM
"""

def outbreak(day):
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75
    else:
        return outbreak(day-1)+outbreak(day-2)+outbreak(day-3)

def main():
    print('OUTBREAK!')
    while True:
        try:
            day = int(input("What day do you want a sick count for?: "))
            assert day >= 1
        except ValueError:
            print('Please enter a valid integer!')
        except AssertionError:
            print('Invalid day')
        else:
            break
    print(f"Total people with flu: {outbreak(day)}")
main()