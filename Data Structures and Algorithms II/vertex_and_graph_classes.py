# We will now use dictionaries to implement the graph abstract data type in Python. 
# We need to have two classes. First, the Graph class that will keep track of the vertices in the graph instance. 
# Second, the Vertex class, which we will use to represent each vertex contained in a graph. 
# Both classes will have methods that allow you to complete the basic operations for interacting with graphs and vertices.

class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight = 0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


# Our graph class's primary purpose is to be a way that we can map vertex names to specific vertex objects. 
# We also want to keep track of the number of vertices that our graph contains using a count property. 

class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values()) # returns a list of all the values available in a given dictionary

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight = 0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()


g = Graph()
for i in range(8):
    g.add_vertex(i)

print(g.vertices)
# {0: <__main__.Vertex object at 0x0000014C179E6F70>, 1: <__main__.Vertex object at 0x0000014C179E6B50>, 2: <__main__.Vertex object at 0x0000014C179E6A60>, 3: <__main__.Vertex object at 0x0000014C179E6A00>, 4: <__main__.Vertex object at 0x0000014C179E69A0>, 5: <__main__.Vertex object at 0x0000014C179E6940>, 6: <__main__.Vertex object at 0x0000014C179E68E0>, 7: <__main__.Vertex object at 0x0000014C179E6880>}

g.add_edge(0,1,3)
g.add_edge(0,7,2)
g.add_edge(1,3,4)
g.add_edge(2,2,1)
g.add_edge(3,6,5)
g.add_edge(4,0,2)
g.add_edge(5,2,3)
g.add_edge(5,3,1)
g.add_edge(6,2,3)
g.add_edge(7,1,4)

for v in g:
    for w in v.get_connections():
        print("( %s, %s )" % (v.get_value(), w.get_value()))

# ( 0, 1 )
# ( 0, 7 )
# ( 1, 3 )
# ( 2, 2 )
# ( 3, 6 )
# ( 4, 0 )
# ( 5, 2 )
# ( 5, 3 )
# ( 6, 2 )
# ( 7, 1 )