for i in range(1,999):
    for j in range(1,999):
        for k in range(1,999):
            if(i+j+k ==1000):
                if( (i*i) + (j*j) == (k*k)) :
                     print(i*j*k)
                     exit()
