# Return a list new list of integers using type(int())

def filter_list_1(l):
    return [x for x in l if type(x) == type(int())]

# Return a list new list of integers using not isinstance(index, type)

def filter_list_2(l):
  return [i for i in l if not isinstance(i, str)]

# Return a list new list of integers using type(x) and str

def filter_list_3(l):
  return [x for x in l if type(x) is not str]

# Return a list new list of integers using list, filter with a lambda with type

def filter_list_4(l):
  return list(filter(lambda x: not type(x) is str, l))

# Return a list new list of integers using isinstance(index, type)

def filter_list_5(l):
  return [e for e in l if isinstance(e, int)]

print(filter_list_1([1,2,'a','b']) == [1,2])
print(filter_list_2([1,'a','b',0,15]) == [1,0,15])
print(filter_list_3([1,2,'aasf','1','123',123]) == [1,2,123])
print(filter_list_4([1,2,'aasf','1','123',123]) == [1,2,123])
print(filter_list_4([1,2,'aasf','1','123',123]) == [1,2,123])
