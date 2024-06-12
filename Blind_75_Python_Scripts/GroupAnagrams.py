from collections import defaultdict

def anagrams(strs):
    res = defaultdict(list) # hash map

    for s in strs:
        count = [0] * 26 # 26 letters in the alphabet, a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1 # using ASCII, we can increment it accordingly, a = 1, b = 2, c = 3

        res[tuple(count)].append(s) # count is a list, cant be a key in the hashmap so we convert count ot tuple

    return res.values()



words = ["eat", "ate", "car", "tae", "acr"]

print(anagrams(words))