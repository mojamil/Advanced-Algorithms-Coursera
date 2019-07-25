# python3
import math
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
    def to_string(self):
        return [self.u,self.v,self.capacity,self.flow]

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph
def get_path(graph, from_,path):
    q=[]
    visited=[False]*graph.size()
    q.append(from_)
    visited[from_]=True
    i=0
    while q:
        

        u=q.pop(0)
        for p in graph.get_ids(u):
            e=graph.get_edge(p)
            if not (visited[e.v]) and e.flow<e.capacity:
                q.append(e.v)
                visited[e.v]=True
                path[e.v]=u
    return visited[graph.size()-1]

def find_edge(graph, from_, to):
    i=0
    for e in graph.edges:
        if (e.u==from_ and e.v==to) and e.capacity>e.flow:
            return (e.capacity-e.flow,i)
        i+=1
    
def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    parentl=[-1]*graph.size()
    while get_path(graph,from_,parentl):
        s=to
        minflow=10000
        path=[]
        while s!=from_:
            minflow=min(minflow,find_edge(graph,parentl[s],s)[0])
            path.append(find_edge(graph,parentl[s],s)[1])
            s=parentl[s]
        for p in path:
            graph.add_flow(p,minflow)
        flow+=minflow
    return flow


if __name__ == '__main__':
    graph = read_data()
    path=[]
    print(max_flow(graph, 0, graph.size() - 1))
