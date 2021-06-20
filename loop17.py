number=int(input("any binary number"))
i=0
decimal=0
while number>0:
    rem=number%10
    decimal=decimal+rem**2
    number=number//10
    i=i+1
print(decimal)

