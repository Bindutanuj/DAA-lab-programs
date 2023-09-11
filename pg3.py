#heap sort
import random
def gen(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)
def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(a,n,largest)
def heap(arr):
    n=len(arr)
    for i in range (n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

a=[]
print("enter limit: ")
n=int(input())
print("the no are: ")
gen(a,n)
print(a)
print("the sorted no are: ")
heap(a)
n=len(a)
print(a)

