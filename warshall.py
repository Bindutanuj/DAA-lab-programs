def transit_clos(reach,n):
    for k in range(n):
         for i in range(n):
               for j in range(n):
                    reach[i][j]=(reach[i][j])or(reach[i][k] and reach[k][j])
graph=[[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]
n=4
transit_clos(graph,n)
for i in range(n):
     print(graph[i])
