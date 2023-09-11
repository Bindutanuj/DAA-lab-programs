def all_pair_sort(dist,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))
graph=[[0,10,100,3],[1,0,5,100],[2,4,0,100],[100,6,100,0]]
n=4
all_pair_sort(graph,n)
for i in range (n):
    print(graph[i])

