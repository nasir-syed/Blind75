def reverse(n):
    # we are basically rotating it to the left kinda
    # like if you were to show numbers to the mirror


    res = 0

    for i in range(32): # 32-bit integer, 32 positions
        bit = (n >> i) & 1
        res | (bit << (31-i))

