# // Joel Silas
# // TE B : Computer Department
# // Roll no. : 3259
# // JSPM's JSCOE, Pune

import collections

def bfs(G,vertices):
    q = collections.deque([vertices[0]])

    visited = [False for _ in range(len(vertices)+1)]
    visited[1] = True

    bfs_traversal = []

    while(q):
        vertex = q.popleft()
        bfs_traversal.append(vertex)

        for j in G[vertex]:
            if(visited[j]==False):
                q.append(j)
                visited[j]=True

    print(bfs_traversal)

def create_graph(vertices,edges):
    G = dict()

    # [G.setdefault(vertex,[]) for vertex in vertices]
    # or
    G = {vertex : [] for vertex in vertices}

    for edge in edges:
        if(edge[1] not in G[edge[0]]):
            G[edge[0]].append(edge[1])
        if(edge[0] not in G[edge[1]]):
            G[edge[1]].append(edge[0])

    print("\nThe graph is : ")

    for key in G:
        print(key,"->",G[key])

    return G

if __name__ == "__main__":
    vertices = []
    edges = []

    v = int(input("Enter the number of vertices of the Graph"))
    for i in range(v):
        vertices.append(int(input("Enter vertex")))

    e = int(input("Enter the number of edges of the Graph"))
    for i in range(e):
        edges.append(list(map(int,input().strip().split())))

    G = create_graph(vertices,edges)
    print("\nBFS is : ")
    bfs(G,vertices)