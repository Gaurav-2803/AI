import sys
import heapq

def find_min(mstSet,key):
    mini_key = sys.maxsize
    vertex=0

    for i in range(n):
        if(mstSet[i]==False and key[i]<mini_key):
            vertex = i
            mini_key = key[i]

    return vertex

if __name__ == "__main__":
    n = int(input("input the number of vertices"))  # input the number of vertices
    m = int(input("input the number of edges"))  # input the number of edges

# to store the graph as an adjacency matrix implemented by the python dictionary
    adj_list = dict()
    print("Enter the edges : ")
    for i in range(m):
        a,b,wt = list(map(int,input().strip().split()))

        if(a in adj_list):
            adj_list[a].append([b, wt])
        else:
            adj_list[a]=[[b,wt]]

        if(b in adj_list):
            adj_list[b].append([a, wt])
        else:
            adj_list[b]=[[a,wt]]

 # heart of the prim's algo
    pq = []
    pq.append([0, 0])
    heapq.heapify(pq)

    parent = [-1 for i in range(n)]
    key = [sys.maxsize for i in range(n)]
    mstSet = [False for i in range(n)]

    key[0] = 0
    parent[0] = -1

    for cnt in range(n-1):
        # u = min_key = find_min(mstSet,key)
        u = heapq.heappop(pq)[1]

        mstSet[u] = True

        for i in adj_list[u]:
            v = i[0]
            weight = i[1]
            if(weight!=0 and mstSet[v]==False and weight<key[v]):
                parent[v] = u
                key[v] = weight
                heapq.heappush(pq,[key[v],v])  # push the (wt and vertex having that wt)

# to display the edges in MST and to calcuAlate total weight of MST
    weight_of_mst = 0

    for i in range(1,n):
        for j in (adj_list[parent[i]]):
            if(j[0]==i):
                wt=j[1]
        print(parent[i],"--",i,"=",wt)
        weight_of_mst += wt

    print("weight of MST =",weight_of_mst)
