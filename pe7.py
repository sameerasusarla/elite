
def isprime(n):
    for j in range(2,int(n**0.5)+1):
         if(n%j==0):
             return False
    return True
count = 0
for i in range(2,1000000):
    if(isprime(i)):
        count = count+1
    if(count==10001):
        print(i)
        exit()

