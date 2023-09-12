def find_set(all_set,key):
    for i in range(len(all_set)):
        if key in all_set[i]:
            return i
def krushkal(edge,v):
    edge.sort(key=lambda x:x[2])
    all_set=[ ]
    for k in vert:
        a=[]
        a.append(k)
        all_set.append(a)
    st_edge=[]
    i=0
    ct=0
    while ct<n-1:
        x=edge[i][0]
        y=edge[i][1]
        s1=find_set(all_set,x)
        s2=find_set(all_set,y)
        if s1!=s2:
            a=[]
            a.append([x,y,edge[i][2]])
            st_edge.append(a)
            all_set[s1]+=all_set[s2]
            del all_set[s2]
            ct+=1
        i+=1
    return st_edge

edge = [['a','b',1],['a','d',2],['a','c',5],['c','d',3]]
vert=['a','b','c','d']
n=len(vert)
st_edge=krushkal(edge,vert)
print(st_edge)


