def ispalindrome(num):
    s= str(num)
    if(s==s[::-1]):
       return True
    else:
       return False
large=0
for i in range(100,999):
    for j in range(100,999):
        t = i*j
        if(ispalindrome(t) and large<t):
           large = t
print(large)
