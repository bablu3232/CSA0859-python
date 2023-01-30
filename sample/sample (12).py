a=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("enter the number:"))
    a.append(b)
a.sort()
print("largest number is :",a[n-1])
