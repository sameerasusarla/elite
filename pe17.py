import inflect
convert = inflect.engine()
sum=0
for num in range(1,1001):
   if num<21 :
       sum+=len(convert.number_to_words(num))
   elif  num<100 :
       if num%10==0 :
           sum+=len(convert.number_to_words(num))
       else :
           rem=num%10
           if rem!=0 :
               sum+=len(convert.number_to_words(rem))
           num=num//10
           num*=10
           if num!=0 :
               sum+=len(convert.number_to_words(num))
   else:
       if num%100==0 :
           sum+=len(convert.number_to_words(num))-1
       else :
           sum+=3
           if(num%100 < 21) :
               rem=num%100
               if rem!=0:
                   sum+=len(convert.number_to_words(rem))
               num=num//100
               num*=100
               sum+=len(convert.number_to_words(num))-1
           else:
               rem=num%10
               if rem!=0 :
                   sum+=len(convert.number_to_words(rem))
               num=num//10
               rem=num%10
               rem*=10
               if rem!=0 :
                   sum+=len(convert.number_to_words(rem))
               num=num//10
               num*=100
               if num!=0 :
                   sum+=len(convert.number_to_words(num))-1
print(sum)
