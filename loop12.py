n = int(input("enter a number"))
# n = num
product = 1
while n > 0:
    rem = n % 10
    product = product * rem
    n = n // 10
print(product)

