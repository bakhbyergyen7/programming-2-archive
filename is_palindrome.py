def is_palindrome(word):
    #your definition
    if len(word) <= 1:
        return True
    elif word[0]!=word[-1]:
        return False
    else:
        var = word[1:len(word)-1]
        return is_palindrome(var)

hi = is_palindrome("Injuu")
print(hi)