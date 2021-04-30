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