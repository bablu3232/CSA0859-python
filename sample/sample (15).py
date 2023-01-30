l=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    e=int(input("enter the elements:"))
    l.append(e)
print(l)
odd=0
even=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    print("odd list is :",odd)
    print("even list is :",even)
