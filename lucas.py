def lucas(num):
    try:
        if num == 0:
            return 2
        elif num == 1:
            return 1
        else:
            return lucas(num-1)+lucas(num-2)
    except:
        print('An exception has occured')

def main():
    try:
        num = int(input("Enter your number:"))
        print(lucas(num))
    except:
        print('Wrong input. Please check it again!')
main()