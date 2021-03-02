sum=""
sum1=""
sum2=0
l1=[]
l2=[]
with open("erg11.txt","r") as f:
    data=f.read()
    for c in data:
        sum=sum+c
print(sum)
for i in sum:
    l1.append(i)
for i in l1:
    if sum2<2:
        if i=='"':
            sum2=sum2+1
        else:
          if sum2==1:
            sum1=sum1+i
    else:
        l2.append(sum1)
        sum1=""
        sum2=0
print("Η λίστα κλειδιών του λεξικού είναι η εξής:")
print(l2)
max=0
for l in l2:
    sum3=0
    for i in l2:
        if l==i:
            sum3=sum3+1
    if sum3>max:
        max=sum3
        j=l
print("Το δημοφιλέστερο κλειδί είναι το",j,"με συχνότητα",max,"φορές.")
