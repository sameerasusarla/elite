fh=open("p022_names.txt")
names=sorted(fh.read().replace('"','"').split(','),key=str)
s=0
count=1
for name in names:
    l = list(name)
    score=0
    for i in l:
        if(i=='"'):
            continue
        else:
            score += (ord(i)-64)  
    s+=(score*count)
    count+=1
print(s)
