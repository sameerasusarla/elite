s=0
for i in range(232792560,100000000000):
    for j in range(1,21):
         if((i%j) !=0):
            break
         if(i%j==0 and j==20):
             s=i
             print(s)
             exit()
