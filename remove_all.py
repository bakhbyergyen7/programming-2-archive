#removes all the repeated values from a list
def remove_all(linkedlist,value):
    i = 0
    while i<linkedlist.length():
        if linkedlist.get_entry(i) == value:
            linkedlist.remove(i)
        else:
            i+=1
    