# Using loops

def dig_pow_1(n, p):
    s = 0
    for i in range(len(str(n))):
        s += int(str(n)[i])**p
        p += 1
    if s/n == s//n: return s/n
    else: return -1
    
# Using enumerate

def dig_pow_2(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

# Using divmod and enumerates

def dig_pow_3(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k

# Usin zip

def dig_pow_4(n, p):
    r = sum([int(i)**j for i,j in zip(str(n),range(p,p+len(str(n))))]) 
    return r//n if r%n == 0 else -1

print(dig_pow_1(89, 1) == 1)
print(dig_pow_2(92, 1) == -1)
print(dig_pow_3(46288, 3) == 51)
print(dig_pow_4(46288, 3) == 51)