def countSubstrings(s):

    res = 0

    for i in range(len(s)):
        l = r = i
        countPali(l, r, s)

        l,r = i, i+1

        countPali(l, r, s)

def countPali(l, r, s):

    while l >= 0 and r < len(S) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1