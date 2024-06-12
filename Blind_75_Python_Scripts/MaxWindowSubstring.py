def searchMax(s, t):

    if t == "": return ""

    countT, window = {}, {} # hashmaps to keep track of the chars

    for c in t:
        countT[c] = 1 + countT.get(c, 0) # if c exists, get its value else its 0

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity") # any num will be less than infinty,
    l = 0
    for r in range(len(s)):
        c = s[r]

        window[c] = 1 + window.get(c, 0)  # add it to the window


        if c in countT and window[c] == countT[c]:
            have += 1  # the char is in window and the countT,

        while have >= need:
            if (r - l + 1) < resLen: # is the size of the window is less than the current lowest window size, and all the chars are present, then we will reassign resLen(the lowest window size)

                res = [l, r] # the window
                resLen = (r - l + 1) # size of the window


            # pop from the left of the window, after the condition has been met,
            # in order to get teh minimum window length with all the chars

            window[s[l]] -= 1

            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    l , r = res
    return s[l:r+1] if resLen != float("infinity") else ""
