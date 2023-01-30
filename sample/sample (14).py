l=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    e=int(input("enter the elements:"))
    l.append(e)
print(l)
s=0
for i in l:
    s=s+i
    print("the sum is ", l," is " ,s)
