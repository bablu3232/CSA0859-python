def sum_arr(arr,size):
    if (size==0):
        return 0
    else:
        return arr[size-1]+sum_arr(arr,size-1)
n=int(input("enter the number of elements:"))
a=[]
for i in range(0,n):
    element=int(input("enter the elements"))
    a.append(element)
print(a)
b=sum_arr (a,n)
print(b)
