from typing import Counter


def most_a(my_list):
    dict = {}
    for word in my_list:
        cnter = 0
        for letter in word.lower():
            if letter == 'a':
                cnter += 1
        dict[word] = cnter
    record = 0
    holder = ''
    for word, dict[word] in dict.items():
        if dict[word] > record:
            record = dict[word]
            holder = word
    return holder

my_list = ['Billie Eilish', 'aaaaaaaaaaaaa' , 'Barack Obama', 'aaa', 'aaaaaaA']

print(most_a(my_list))

print(dict)