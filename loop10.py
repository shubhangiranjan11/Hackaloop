user=int(input("any number"))
i=0
sum=0
while user>0:
    var=user%10
    i=(i*10)+var
    user=user//10
print(i)

