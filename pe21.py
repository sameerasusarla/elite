def sumofdivisors(num):
    pdivisors=[]
    for i in range(1,num):
        if num%i == 0:
            pdivisors.append(i)
    return sum(pdivisors)        

def isamicable(num):
    num1=sumofdivisors(num)
    num2=sumofdivisors(num1)
    if num == num2 and num!= num1 :
        return True
    return False

s=0
for i in range(1,10001):
    if isamicable(i) == True:
        s=s+i
print(s)

