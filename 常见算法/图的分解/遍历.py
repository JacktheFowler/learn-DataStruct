"""
explore G, v

parameter 
G (V, E) V nodes E edges{adjancy matrix}
v nodes to be started

Return
all reachable nodes

visited[v]=true
previsited(v)
for each (u, v) in edges:
if not visited: explore(u)
postvisted(v)

time usage O(V+E)
"""

"""
ex 1->2 1->3 2->4 3->4 4->5 [[1, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
right return 1->2->4->5 3
"""

def explore(adjancy, v):
    visited=[False]*len(adjancy)
    res=[]
    def dfs(v):
        res.append(v)
        visited[v]=True
        for i, connect in enumerate(adjancy[v]):
            if connect and (not visited[i]):
                dfs(i)
    dfs(v)
    return res

adjancy=[[1, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
res=explore(adjancy, 0)
print(res)

