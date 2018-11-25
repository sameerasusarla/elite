"""n=int(input())"""
l1=[]
size = 0
for n in range(13,1000000):
    l1.append(n)
    while(n!=1):
        if(n%2 ==0):
            n = n//2
        else :
            n = (3*n)+1
        l1.append(n)
    if(size<len(l1)):
      size = len(l1)
      l2 = l1
    l1=[]
print(l2)
print(size)

