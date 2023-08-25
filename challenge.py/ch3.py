a= list(input("give me a list"))

def t (c):
    dic={}
    b= set(c)
    for b in c:
        d= a.count(b)
        j=dict({b:d})
        dic.update(j)
    print(dic)
t(a)
    
    
