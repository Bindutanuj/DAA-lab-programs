def dfs(graph,start,path):
    s=[start]
    while s:
        node= s.pop()
        if node not in path:
            path.append(node)
            for v in graph[node]:
                if v not in path:
                    s.append(v)

graph={1:[2,4],2:[3],3:[2,4],4:[1,2]}
#graph={1:[4,3,5],2:[3,1],3:[5],4:[3,1],5:[4,2]}
path=[]
dfs(graph,1,path)
print(path)
