
# coding: utf-8

# In[1]:


class Graph(object):
    def __init__(self, vertices=set(), edges=[]):
        self.vertices = set()
        for v in vertices:
            self.addVertex(v)
        
        self.edges = []
        for e in edges:
            self.addEdge(e)
    
    
    def getVertices(self):
        return self.vertices
    
    
    def addVertex(self, vertex):
        self.vertices.add(vertex)
    
    
    def removeVertex(self, vertex):
        self.vertices.remove(vertex)
        for t in self.edges:
            if vertex == t[0] or vertex == t[1]:
                self.edges.remove(t)
    
    
    def getEdges(self):
        return self.edges
    
    
    def addEdge(self, edge):
        self.vertices.add(edge[0])
        self.vertices.add(edge[1])
        self.edges.append((edge[0], edge[1], edge[2]))
    
    
    def removeEdge(self, edge):
        self.edges.remove(edge)
    
    
    def getNeighbours(self, vertex):
        neighbours = set()
        for t in self.edges:
            if vertex == t[0]:
                neighbours.add(t[1])
            if vertex == t[1]:
                neighbours.add(t[0])
        return neighbours
    
    
    def getOutEdges(self, vertex):
        outEdge = []
        for t in self.edges:
            if vertex == t[0]:
                outEdge.append(t)
        return outEdge
    
    
    def getInEdges(self, vertex):
        inEdge = []
        for t in self.edges:
            if vertex == t[1]:
                inEdge.append(t[0])
        return inEdge
    
    
    def dijkstra(self, source):
        vertices = self.getVertices()
        if source not in vertices:
            return
        
        dist = {} # Distance from source to key
        Q = {} # Same as dist but only unvisited nodes
        outEdges = {} # List of outedges from key
        
        for v in vertices:
            dist[v] = float('inf') # Start with infinity distance
            Q[v] = float('inf')
            outEdges[v] = []
        for e in self.getEdges():
            outEdges[e[0]].append(e)
        
        dist[source] = 0
        Q[source] = 0
        
        while Q:
            u = min(Q, key=Q.get) # Closest node
            del Q[u]
            for e in outEdges[u]:
                v = e[1] # Destination
                distanceToV = e[2]
                
                alt = dist[u] + distanceToV
                if alt < dist[v]:
                    dist[v] = alt
                    Q[v] = alt
        
        return dist
    
    
    def pagerank(self, personalised=[], a=0.15, maxIter=15):
        vertices = self.getVertices()
        for v in personalised:
            if v not in vertices:
                raise Exception('No vertex {} exists'.format(v))
        E = {} # For personalised pagerank
        ranks = {} # PR value of key
        incomingEdgesVertex = {} # List of vertices with citations to key
        outDegrees = {} # Number of citations from key
        
        for v in vertices:
            E[v] = 0 if len(personalised) else 1
            ranks[v] = 1 # All PR start with 1
            incomingEdgesVertex[v] = []
            outDegrees[v] = 0
        for v in personalised:
            E[v] = 1/len(personalised)
        for e in self.getEdges():
            incomingEdgesVertex[e[1]].append(e[0])
            outDegrees[e[0]] += 1
        
        
        for _ in range(maxIter):
            for v in vertices:
                rank = 0
                for u in incomingEdgesVertex[v]:
                    rank += ranks[u]/outDegrees[u]
                ranks[v] = E[v] * a + (1-a)*rank
        
        return ranks


# In[2]:


if __name__ == '__main__':
    import string
    
    # Vertices
    vertices = []
    vertices.extend([i for i in string.ascii_uppercase[:14]])
    
    # Edges
    edges = []
    edges.extend([
        ('A', 'B', 2),
        ('A', 'C', 10),
        ('B', 'D', 10),
        ('B', 'E', 8),
        ('C', 'G', 5),
        ('E', 'F', 6),
        ('F', 'C', 1),
        ('G', 'H', 11),
        ('G', 'J', 9),
        ('H', 'I', 4),
        ('I', 'K', 4),
        ('J', 'K', 8),
        ('L', 'M', 4),
        ('L', 'N', 4),
        ('M', 'N', 4)])
    
    '''
    A → B
    ↓   ↓ ↘
    C   D   E
    ↓ ↖   ↙
    ↓   F
    ↓
    G → H → I
      ↘     ↓
        J → K
    '''
    
    source = 'A'
    dg = Graph(vertices, edges)
    dist = dg.dijkstra(source)
    
    print("From {} (Directed):".format(source))
    print("{:<5} {:<15}".format('To', 'Distance'))
    from operator import itemgetter
    for k, v in sorted(dist.items(), key=itemgetter(1)):
        print("{:<5} {:<15}".format(k, v))
    
    print()
    
    pr = dg.pagerank()
    print("Pagerank (Directed):")
    print("{:<5} {:<15}".format('Node', 'Pagerank'))
    for k, v in sorted(pr.items(), key=itemgetter(1), reverse=True):
        print("{:<5} {:<15}".format(k, v))
    
    print()
    
    pr = dg.pagerank([source])
    print("Personalised pagerank for {} (Directed):".format(source))
    print("{:<5} {:<15}".format('Node', 'Pagerank'))
    for k, v in sorted(pr.items(), key=itemgetter(1), reverse=True):
        print("{:<5} {:<15}".format(k, v))
    
    print()
    
    edges.extend([(t[1], t[0], t[2]) for t in edges]) # Make bidirected graph
    
    bg = Graph(vertices, edges)
    dist = bg.dijkstra(source)
    
    print("From {} (Bidirected):".format(source))
    print("{:<5} {:<15}".format('To', 'Distance'))
    from operator import itemgetter
    for k, v in sorted(dist.items(), key=itemgetter(1)):
        print("{:<5} {:<15}".format(k, v))
    
    print()
    
    pr = bg.pagerank()
    print("Pagerank (Bidirected):")
    print("{:<5} {:<15}".format('Node', 'Pagerank'))
    for k, v in sorted(pr.items(), key=itemgetter(1), reverse=True):
        print("{:<5} {:<15}".format(k, v))
    
    print()
    
    pr = bg.pagerank([source])
    print("Personalised pagerank for {} (Bidirected):".format(source))
    print("{:<5} {:<15}".format('Node', 'Pagerank'))
    for k, v in sorted(pr.items(), key=itemgetter(1), reverse=True):
        print("{:<5} {:<15}".format(k, v))

