fact=1
for i in range(1,101):
    fact=fact*i
sum=0
while fact!=0:
    rem=fact%10
    sum=sum+rem
    fact=fact//10

print(sum)
