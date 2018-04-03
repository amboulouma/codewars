# Using calculus

from math import sqrt

def find_nb(m):
    n = (sqrt(1 + 4*2*sqrt(m)) - 1)/2
    if m == sum(i**3 for i in range(int(n) + 1)): return int(n)
    else: return -1
    
# Using loop

def find_nb(m):
    i,sum = 1,1
    while sum < m:
        i+=1
        sum+=i**3
    return i if m==sum else -1
    
print(find_nb(4183059834009) == 2022)
print(find_nb(24723578342962) == -1)
print(find_nb(135440716410000) == 4824)
print(find_nb(40539911473216) == 3568)
print(find_nb(26825883955641) == 3218)