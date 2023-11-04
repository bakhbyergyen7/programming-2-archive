#Constant time complexity

for num in range(10):
    print(num)

# This 'algorithm' is influenced by
# some n, and it scales in a linear
# way
n = ???
for num in range(n):
    print(num)

# This 'algorithm' scales quadratically

n = ???

for i in range(n):
    for j in range(n):
        print(i,j)