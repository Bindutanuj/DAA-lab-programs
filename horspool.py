def horspool(text,pattern):
    m=len(text)
    n=len(pattern)
    if m<n:
        return -1
    shift=[n]*250
    for i in range(n-1):
        shift[ord(pattern[i])]=n-i-1
    pos=0
    while pos<=m-n:
        j=n-1
        while j>=0 and pattern[j]==text[pos+j]:
            j=j-1
        if j==-1:
            return pos
        else:
            pos+=shift[ord(text[pos+n-1])]
    return -1

text=input("enter the string : ")
pattern=input("enter the pattern : ")
pos=horspool(text,pattern)
if(pos>=0):
    print("the pattern is found in : ",pos+1)
else:
    print("the pattern is not found in  ")