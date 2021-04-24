# What Are Graphs?

# Graphs are collections of related data. 
# They’re like trees, except connections can be made from any node to any other node, even forming loops. 
# By this definition, all trees are graphs, but not all graphs are trees.

# We call the nodes in a graph vertexes (or vertices or verts), and we call the connections between the verts edges.
# An edge denotes a relationship or linkage between the two verts.

# Graphs can represent any multi-way relational data.
# A graph could show a collection of cities and their linking roads.
# It could show a collection of computers on a network.


# Directed and Undirected Graphs
# If we could describe the relationship as "one way", then a directed graph makes the most sense. 
# For example, representing the owing of money to others (debt) with a directed graph would make sense.

# Directed graphs can also be bidirectional. 
# For example, road maps are directed since all roads are one-way; however, most streets consist of lanes in both directions.

# If the relationship's nature is a mutual exchange, then an undirected graph makes the most sense. 
# For example, we could use an undirected graph to represent users who have exchanged money in the past. 
# Since an "exchange" relationship is always mutual, an undirected graph makes the most sense here.

# Cyclic and Acyclic Graphs
# If you can form a cycle (for example, follow the edges and arrive again at an already-visited vert), the graph is cyclic
# Note: any undirected graph is automatically cyclic since you can always travel back across the same edge.

# If you cannot form a cycle (for example, you cannot arrive at an already-visited vert by following the edges), we call the graph acyclic

# Weighted graphs have values associated with the edges. We call the specific values assigned to each edge weights.


# The weights represent different data in different graphs. In a graph representing road segments, the weights might represent the length of the road. 
# The higher the total weight of a route on the graph, the longer the trip is. 
# The weights can help decide which particular path we should choose when comparing all routes.

# We can further modify weights. 
# For example, if you were building a graph representing a map for bicycle routes, we could give roads with bad car traffic or very steep inclines unnaturally large weights. 
# That way, a routing algorithm would be unlikely to take them. (This is how Google Maps avoids freeways when you ask it for walking directions.)

# Note: Djikstra's Algorithm is a graph search variant that accounts for edge weights.

# Directed Acyclic Graphs (DAGs)
# A directed acyclic graph (DAG) is a directed graph with no cycles. 
# In other words, we can order a DAG’s vertices linearly in such a way that every edge is directed from earlier to later in the sequence.

# Below is a small list of possible applications:

# A spreadsheet where a vertex represents each cell and an edge for where one cell's formula uses another cell's value.
# The milestones and activities of largescale projects where a topological ordering can help optimize the projects' schedule to use as little time as possible.
# Collections of events and their influence on each other like family trees or version histories.

# It is also notable that git uses a DAG to represent commits. A commit can have a child commit, or more than one child commit (in a branch). A child could come from one parent commit or two (in the case of a merge). But there’s no way to go back and form a repeating loop in the git commit hierarchy.

