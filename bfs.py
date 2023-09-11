def bfs(graph,start,path):
    q=[start]
    path.append(start)
    while q:
        node=q.pop(0)
        for v in graph[node]:
            if not v in path:
                 path.append(v)
                 q.append(v)
graph={1:[2,4],2:[3],3:[2,4],4:[1,2]}
path=[]
bfs(graph,1,path)
print(path)
