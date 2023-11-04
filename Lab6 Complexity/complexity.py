from linked_list import LinkedList
from linked_queue import Queue
from linked_stack import Stack

import time

def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

# Popping a single item from a stack

print("Beginning the timing code...")


my_stack = Stack()

time_taken = []


for i in range(1, 101):
    for j in range(1000*i):
        my_stack.push(j)
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    my_stack.pop()
    end_time = time.perf_counter_ns()
    time_taken.append(end_time-start_time)

print("Single Item From a Stack Starts")
for timing in time_taken:
    print(timing)
    # print(nanosec_to_sec(timing))
print("Single Item From a Stack Ends")

# Popping all items from a stack

time_taken1 = []

for i in range(1, 101):
    for j in range(1000*i):
        my_stack.push(j)
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    for j in range(1000*i):
        my_stack.pop()
    end_time = time.perf_counter_ns()
    time_taken1.append(end_time-start_time)

print("All Items From a Stack Starts")

for timing in time_taken1:
    print(timing)
    # print(nanosec_to_sec(timing))

print("All Items From a Stack Ends")

# Queue's enqueue
my_queue = Queue()
time_taken2 = []

for i in range(1, 101):
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    for j in range(1000*i):
        my_queue.enqueue(j)
    end_time = time.perf_counter_ns()
    time_taken2.append(end_time-start_time)

print("Enqueue Starts")

for timing in time_taken2:
    print(timing)
    # print(nanosec_to_sec(timing))

print("Enqueue Ends")

# Linked List get_entry at specifically index 0

time_taken3 = []

for i in range(1, 101):
    my_list = LinkedList()
    for j in range(1000*i):
        my_list.insert(0, j)
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    my_list.get_entry(0)
    end_time = time.perf_counter_ns()
    time_taken3.append(end_time-start_time)

print("get_entry at index 0 Starts")

for timing in time_taken3:
    print(timing)
    # print(nanosec_to_sec(timing))

print("get_entry at index 0 Ends")

# Linked List get_entry at specifically the last index


time_taken4 = []

for i in range(1, 101):
    my_list1 = LinkedList()
    for j in range(1000*i):
        my_list1.insert(0, j)
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    my_list1.get_entry(my_list1.length()-1)
    end_time = time.perf_counter_ns()
    time_taken4.append(end_time-start_time)

print("get_entry at last index Starts")

for timing in time_taken4:
    print(timing)
    # print(nanosec_to_sec(timing))

print("get_entry at last Ends")

# Printing all elements in a LinkedList using get_entry


time_taken5 = []

for i in range(1, 101):
    my_list2 = LinkedList()
    for j in range(1000*i):
        my_list2.insert(0, j)
    start_time = time.perf_counter_ns() #Remember to use process_time_ns if running on linux
    for j in range(1000*i):
        elmnt = my_list2.get_entry(j)
        print(elmnt)
    end_time = time.perf_counter_ns()
    time_taken5.append(end_time-start_time)

print("Printing all elements Starts")

for timing in time_taken5:
    print(timing)

print("Printing all elements Ends")