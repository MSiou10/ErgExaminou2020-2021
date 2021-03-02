list=[]
sum=0
sum1=0
sum2=0
with open('erg10.txt','r') as f:
    data=f.read()
    for c in data:
        sum2=sum2+1
        if c=="{":
            sum=sum+1
        if c=="[":
            sum=sum+1
            sum1=sum1+1
    if sum2<=2:
        print("Το μεγαλύτερο βάθος του λεξικού είναι:",0)
    else:
        if sum1>=2:
            print("Το μεγαλύτερο βάθος του λεξικού είναι:",sum-1)
        else:
            print("Το μεγαλύτερο βάθος του λεξικού είναι:",sum)
