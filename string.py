def unique(st):
    d={}
    for i in st:
        d[i]=d.get(i,0)+1
    for j in range(len(st)):
        if d[st[i]]==1:
            return j
    return -1
n=input()    
print(unique(n))            
