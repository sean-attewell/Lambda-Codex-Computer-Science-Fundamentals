# Another method we can use when searching a graph is a depth-first search (DFS). 
# This searching algorithm "dives" "down" the graph as far as it can before backtracking and exploring another branch.

# The algorithm never attempts to explore a vert it has already explored or is exploring.

# The visitation order is shown in graph_DFS_order.jpg
# We followed the edges represented with thicker black arrows. 
# We did not follow the edges represented with thinner grey arrows because we already visited their destination nodes.

# The exact order will vary depending on which branches get taken first and which vertex is the starting vertex.

# Applications of DFS
# DFS is often the preferred method or exploring a graph if we want to ensure we visit every node in the graph. 
# For example, let's say that we have a graph representing all the friendships in the entire world. 
# We want to find a path between two known people, Andy and Sarah. 
# If we used a depth-first search in this scenario, we could end up exceptionally far away from Andy while still not finding a path to Sarah. 
# Using a DFS, we will eventually find the path, but it won't find the shortest route, and it will also likely take a long time.

# What about a genuine use case for DFS? Here are a few examples:

# Finding Minimum Spanning Trees of weighted graphs
# Pathfinding
# Detecting cycles in graphs
# Topological sorting, useful for scheduling sequences of dependent jobs
# Solving and generating mazes

# Again, as we explore the graph, it is useful to color verts as we arrive at them and as we leave them behind as "already searched".
# Unvisited verts are white, verts whose neighbors are being explored are gray, and verts with no unexplored neighbors are black.

# Recursion
# Since DFS will pursue leads in the graph as far as it can, and then "back up" to an earlier branch point to explore that way, 
# recursion is an excellent approach to help "remember" where we left off.

# Pseudo-code for DFS

# DFS(graph):
#     for v of graph.verts:
#         v.color = white
#         v.parent = null

#     for v of graph.verts:
#         if v.color == white:
#             DFS_visit(v)

# DFS_visit(v):
#     v.color = gray

#     for neighbor of v.adjacent_nodes:
#         if neighbor.color == white:
#             neighbor.parent = v
#             DFS_visit(neighbor)

#     v.color = black


# The first function, DFS() takes the graph as a parameter and marks all the verts as unvisited (white). 
# It also sets the parent of each vert to null
# The next loop in this function visits each vert in the graph, and if it is unvisited, 
# it passes that vert into our second function DFS_visit().

# DFS_visit() starts by marking the vert as gray (in the process of being explored). 
# Then, it loops through all of its unvisited neighbors. 
# In that loop, it sets the parent and then makes a recursive call to the DFS_visit(). 
# Once it's done exploring all the neighbors, it marks the vert as black (visited).

# https://brilliant.org/wiki/depth-first-search-dfs/

# Implementing depth first search:

# The depth-first search algorithm on a graph starts at an arbitrary vertex in the graph and explores as far as possible down each branch before backtracking. 
# So, you start at the starting vertex, mark it as visited, and then move to an adjacent unvisited vertex. 
# You continue this loop until every reachable vertex is visited.

# Requires a stack rather than a list (FIFO) like BFS
# So with a recursive implementation you're using the call stack as your data structure essentially.

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
        return iter(self.vertices.values())

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

    def depth_first_search(self, vertex, visited = set()):
        visited.add(vertex)
        for next_vert in vertex.get_connections():
            if next_vert not in visited:
                self.depth_first_search(next_vert, visited)
