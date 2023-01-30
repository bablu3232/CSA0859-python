num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
sum=0
product=0
print("the common divisors for ",num1," and ",num2," are ")
for i in range(1,min(num1,num2)+1): 
    if num1%i==num2%i==0:
        sum=num1+num2
        product=num1*num2
if sum>0:
    if (product%sum==0):
        print("yeah")
    else:
        print("nah")
else:
    print("invalid input")

