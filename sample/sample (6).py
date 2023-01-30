a=[]
n=int(input("enter the number of elements in list: "))
for x in range(0,n):
    element=int(input("enter the element"+str(x+1)+ ":"))
    a.append(element)
b=set()
un=[]
for x in a:
    if x not in b:
        un.append(x)
        b.add(x);
    print("non-duplicate items:")
    print(un)
