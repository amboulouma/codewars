
def order(sentence):
    if sentence != "": 
        nl = ['']*len(sentence.split(' '))
        for i in sentence.split(' '):
            for j in i:
                if j.isdigit():
                    nl[int(j)-1] = i
        return " ".join(nl)
    else: return ""
  
print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")