# Count vowels using sum of list of map of count any vowel in the string

def getCount_1(s):
    return sum(list(map(s.count, ['a', 'i', 'e', 'o', 'u'])))

# Count vowels using sum of ones for every vowels in the string

def getCount_2(inputStr):
    return sum(1 for i in inputStr if i in "aeiouAEIOU")

def getCount_3(s):
    return sum(c in 'aeiou' for c in s)

print(getCount_1("abracadabra") == 5)
print(getCount_2("abracadabra") == 5)
print(getCount_3("abracadabra") == 5)