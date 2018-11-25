def isprime(num):
   c=0
   for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            c+=1
            break
   if(c!=0):
        return False
   else:
        return True
sum2=0
sum1=0
for i in range(2,1000000):
    if(isprime(i)):
         sum1 =sum1+i
for i in range(1000000,2000000):
    if(isprime(i)):
         sum2 =sum2+i
print(sum1+sum2)
