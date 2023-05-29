# // Joel Silas
# // TE B : Computer Department
# // Roll no. : 3259
# // JSPM's JSCOE, Pune

def dfs(G,node,visited,dfs_traversed):

    dfs_traversed.append(node)
    visited[node] = True

    for vertex in G[node]:
        if(visited[vertex]==False):
            dfs_traversed = dfs(G,vertex,visited,dfs_traversed)

    return dfs_traversed

def create_graph(vertices, edges):
    G = dict()

    # [G.setdefault(vertex,[]) for vertex in vertices]
    # or
    G = {vertex: [] for vertex in vertices}

    for edge in edges:
        if (edge[1] not in G[edge[0]]):
            G[edge[0]].append(edge[1])
        if (edge[0] not in G[edge[1]]):
            G[edge[1]].append(edge[0])

    print("\nThe graph is : ")

    for key in G:
        print(key, "->", G[key])

    return G

if __name__ == "__main__":
    vertices = []
    edges = []

    v = int(input("Enter the number of vertices of the Graph"))
    for i in range(v):
        vertices.append(int(input("Enter vertex")))

    e = int(input("Enter the number of edges of the Graph"))
    for i in range(e):
        edges.append(list(map(int, input().strip().split())))

    G = create_graph(vertices, edges)

    visited = [False for i in range(len(vertices)+1)]

    print("\nDFS is :")
    print(dfs(G, vertices[0], visited , []))