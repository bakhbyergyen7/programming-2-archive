def gib(n):
    if n == 0:
        return 3
    elif n == 1:
        return 10
    else:
        return gib(n-2)+gib(n-1)