a=[]
n=int(input("enter the list:"))
for x in range(0,n):
    e=int(input("enter the elements:"+str(x+1)+":"))
    a.append(e)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)
