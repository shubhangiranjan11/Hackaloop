
n=int(input("enter the num"))
a=n
i=0
sum=0
while n>0:
    rev=n%10
    sum=sum*10+rev
    n=n//10
if a==sum:
    print("palondrome")
else:
    print("not")

