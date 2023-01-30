a=[]
n=int(input("no. of elements:"))
for i in range (1,n+1):
    b=int(input("the elements:"))
    a.append(b)
k=0
num=int(input("enter the number to be counte:"))
for j in a:
    if (j==num):
        k=k+1
print("number of time ",num," appears is ",k)
