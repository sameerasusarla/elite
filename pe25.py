f1=1
f2=1
for i in range(3,4783):
    num = f1 + f2
    f1=f2
    f2=num
    l=[int(x) for x in str(num)]
    if i ==12 :
        print(num)
    if len(l) >= 1000 :
        print(i)
        break

        
