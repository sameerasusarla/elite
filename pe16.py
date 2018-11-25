num = 2**1000
s = [int(x) for x in str(num)]
sum=0
for i in range(0,len(s)):
    sum+=s[i]
print(sum)
