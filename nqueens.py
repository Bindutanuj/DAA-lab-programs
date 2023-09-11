from math import *

x = {}
n = 4

def place(k, i):
    if i in x.values():
        return False
    j = 1
    while j < k:
        a = x[j]
        if abs(a - i) == abs(j - k):
            return False
        j = j + 1
    return True

def clearBlocks(k):
    for i in range(k, n + 1):
        x[i] = None

def Nqueens(k):
    for i in range(1, n + 1):
        clearBlocks(k)
        if place(k, i):
            x[k] = i
            if k == n:
                for j in range (1, n + 1):
                    print("Place Queen at position:", x[j])
                print("...........................")
            else:
                Nqueens(k + 1)

# --------------Driver code--------------
Nqueens(1)
