import random
import time
def gen(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)
def partition(a,left,right):
    key=a[left]
    i=left+1
    j=right
    while True:
        while a[i]<key and i<right:
            i=i+1
        while a[j]>key and j>left:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
        else:
            break
    a[left],a[j]=a[j],a[left]
    return j

def quick(a,low,high):
    if low<high:
        k=partition(a,low,high)
        quick(a,low,k-1)
        quick(a,k+1,high)

a=[]
print("enter the limit : ")
n=int(input())
gen(a,n)
print("the no are : ")
print(a)
start=time.time
quick(a,0,n-1)
end=time.time
print("sorted no are : ")
print(a)
print("the required to sorted : ",(end-start))

