l1=[]
l2=[]
sum=""
sum1=0
sum2=""
sum3=""
sum4=""
with open('erg12.txt','r') as f:
    data=f.read()
    for c in data:
        k=ord(c)
        print("Ο κατοπτρικός χαρακτήρας του",c,"είναι ο",chr(128-k))
        sum=sum+c
x=sum.split()
for i in x:
    sum2=""
    y=i[::-1]
    for j in y:
        sum2=sum2+chr(128-ord(j))
    l1.append(sum2)
for i in l1:
    if sum1<2:
        sum1=sum1+1
        sum3=sum3+" "+i
    else:
        sum1=0
print("Το κατοπτρικό κείμενο με ανάποδη σειρά συντάσσεται ως εξής:")
print(sum3)
