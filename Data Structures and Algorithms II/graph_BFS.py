# One method we can use when searching a graph is a breadth-first search (BFS). 
# This sorting algorithm explores the graph outward in rings of increasing distance from the starting vertex.

# The algorithm never attempts to explore a vert it has already explored or is currently exploring.

# The image "graph_BFS_order.jpg" shows visitation order when startting from the upper left.
# We followed the edges represented with thicker black arrows. 
# We did not follow the edges represented with thinner grey arrows because we already visited their destination nodes.

# The exact order will vary depending on which branches get taken first and which vertex is the starting vertex.

# Note: it's essential to know the distinction between a breadth-first search and a breadth-first traversal. 
# A breadth-first traversal is when you visit each vertex in the breadth-first order and do something during the traversal. 
# A breadth-first search is when you search through vertexes in the breadth-first order until you find the target vertex. 
# A breadth-first search usually returns the shortest path from the starting vertex to the target vertex once the target is found.

# Pathfinding, Routing
# Find neighbor nodes in a P2P network like BitTorrent
# Web crawlers
# Finding people n connections away on a social network
# Find neighboring locations on the graph
# Broadcasting in a network
# Cycle detection in a graph
# Finding Connected Components
# Solving several theoretical graph problems

# As we explore the graph, it is useful to color verts as we arrive at them and as we leave them behind as "already searched".
# Unvisited verts are white, verts whose neighbors are being explored are gray, and verts with no unexplored neighbors are black.

# In a BFS, it's useful to track which nodes we still need to explore. 
# For example, in the diagram above, when we get to node 2, we know that we also need to explore nodes 3 and 4.

# We can track that by adding neighbors to a queue (which remember is first in, first out), and then explore the verts in the queue one by one.


# Let's explore some pseudo-code that shows a basic implementation of a breadth-first-search of a graph

# BFS(graph, startVert):
#     for v of graph.vertexes:
#         v.color = white

#     startVert.color = gray
#         queue.enqueue(startVert)

#     while !queue.isEmpty():
#         u = queue[0]  // Peek at head of the queue, but do not dequeue!

#         for v of u.neighbors:
#             if v.color == white:
#                 v.color = gray
#                 queue.enqueue(v)

#         queue.dequeue()
#         u.color = black


# You can see that we start with a graph and the vertex we will start on. 
# The very first thing we do is go through each of the vertices in the graph and mark them with the color white. At the outset, we mark all the verts as unvisited.

# Next, we mark the starting vert as gray. We are exploring the starting verts’ neighbors. 
# We also enqueue the starting vert, which means it will be the first vert we look at once we enter the while loop.

# The condition we check at the outset of each while loop is if the queue is not empty. 
# If it is not empty, we peek at the first item in the queue by storing it in a variable.

# Then, we loop through each of that vert's neighbors and:

# We check if it is unvisited (the color white).
# If it is unvisited, we mark it as gray (meaning we will explore its neighbors).
# We enqueue the vert.
# Next, we dequeue the current vert we've been exploring and mark that vert as black (marking it as visited).

# We continue with this process until we have explored all the verts in the graph.


# Adding it as a method to the Graph Class:

from queues import Queue

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

class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values()) # .values() returns a list of all the values available in a given dictionary

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

    def breadth_first_search(self, starting_vert):
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vert)
        visited.add(starting_vert)
        while to_visit.size() > 0:
            current_vert = to_visit.dequeue()
            for next_vert in current_vert.get_connections():
                if next_vert not in visited:
                    visited.add(next_vert)
                    to_visit.enqueue(next_vert)

