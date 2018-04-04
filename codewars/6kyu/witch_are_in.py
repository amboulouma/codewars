# Using set

def in_array_1(a1, a2): 
    s = set()
    for a in a1:
        for b in a2:
            if a in b:
                s.add(a)
    return sorted(list(s))

# Using any

in_array_2 = lambda a1, a2: sorted({sub for sub in a1 if any(sub in s for s in a2)})

# Using lists

def in_array_3(array1, array2):
    # your code
    res = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and not a1 in res:
                res.append(a1)
    res.sort()
    return res

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

print(in_array_1(a1, a2) == r)
print(in_array_2(a1, a2) == r)
print(in_array_3(a1, a2) == r)