f=0
l=1
m=0
sum=0
for i in range(0,100):
    m=f+l
    f=l
    l=m
    if(m>4000000):
       break;
    elif(m%2==0):
         sum+=m
print(sum)	
