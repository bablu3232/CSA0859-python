a=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("enter the number:"))
    a.append(b)
print(a)
s=0
for i in a:
    s=s+i
    print("sum of all integes present in",n," is ",s)
