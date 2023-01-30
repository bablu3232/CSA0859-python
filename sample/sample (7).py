a=[]
n=int(input("enter the number of elements in list:"))
for x in range(0,n):
    ele=int(input("enter the elements"+str(x+1)+":"))
    a.append(ele
             )
temp=a[0]
a[0]=a[n-1]
a[n-1]==temp
print("new list is :")
print(a)
