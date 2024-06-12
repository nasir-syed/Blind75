def isPalindrome(s):

     # newStr = ""
     #
     # for c in s:
     #     if c.isalnum():
     #         newStr += c.lower()
     #
     # return newStr == newStr[::-1]

    # the above is kinda iffy, has a lot of builtin functions and room for error


    l, r = 0, len(s)-1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
            # makes sure the left pointer is at a alphanumeric char, if not, increment
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower != s[r].lower:
            return False

        l, r = l + 1, r - 1  # update the pointers after each iteration even if they are alphanumeric

    return True
    # if the while loop is executed successfully, then it is palindrome

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or \
            ord('a') <= ord(c) <= ord('z') or \
            ord('0') <= ord(c) <= ord('9'))
         # if the char is alphanumeric ( a capital or lowercase letter, or a number) this if statement is executed


s = "racecar"
print(isPalindrome(s))

t = "nay"
print(isPalindrome(t))