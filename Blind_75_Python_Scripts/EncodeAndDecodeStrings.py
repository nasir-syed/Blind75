def encode(strs):
    res = " "
    for s in strs:
        res += str(len(s)) + "#" + s



def decode(s):

    res, i = [], 0

    while i < len(s):
        j = i
        while str[j] != "#":
            j += 1  # it could be a long integer like 17 or 26

        length = int(str[i:j])  # the length of the word coming up
        res.append(str[j + 1: j + 1 + length]) # this will append the string to res list
        i = j + 1 + length # going to the next word
    return res


