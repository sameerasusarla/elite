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
large=0
for i in range(2,1000000):
     if(isprime(i)):
        if(600851475143%i == 0):
               large = i
               print(large)
