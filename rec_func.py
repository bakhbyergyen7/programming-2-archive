
def rec_func(i):

    if i < 3:     
        print(i)
        rec_func(i+1) # recursive call

# Goal: Write a recursive factorial
def rec_fact(num):
    if num <= 1:
        return 1
    else:
        return num*rec_fact(num-1)
def main():
    #rec_func(0) #initial call
    print(rec_fact(6))
main()