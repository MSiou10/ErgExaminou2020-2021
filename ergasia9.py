
h=0
l=list()

with open('erg9.txt','r') as f:
 data=f.read()
 for c in data:
    k=ord(c)
    if k%2==1 or k==1:
       l.append(c)

 print(l)

 for i in l:
     g=0
     for j in l:
         if i==j:
             g=g+1
     a=g-1
     for v in range(a):
         l.remove(i)
print(l)
for i in l:
    h=0
    for c in data:
        if ord(i)==ord(c):
            h=h+1
    g=h/len(l)*100//1+1
    print(i,":",int(g)*"*")
