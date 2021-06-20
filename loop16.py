num=int(input("any number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")
    

