# Graph Representations
# Two common ways to represent graphs in code are adjacency lists and adjacency matrices. 
# Both of these options have strengths and weaknesses

# Adjacency List

class Graph_Adjacency_List:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }

# Notice that this adjacency list doesn't use any lists. 
# The vertices collection is a dictionary which lets us access each collection of edges in O(1) constant time.
# Because a set contains the edges, we can check for edges in O(1) constant time.

# Here is the representation of the graph above in an adjacency matrix:

class Graph_Adjacency_Matrix:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]

# We represent this matrix as a two-dimensional array–a list of lists. 
# With this implementation, we get the benefit of built-in edge weights. 
# 0 denotes no relationship, but any other value represents an edge label or edge weight.
# The drawback is that we do not have a built-in association between the vertex values and their index.

# In practice, implementing both the adjacency list and adjacency matrix would contain more information by including Vertex and Edge classes.

# Shorthand	
# V	Total number of vertices in the graph
# E	Total number of edges in the graph
# e	Average number of edges per vertex

# Space Complexity
# Adjacency Matrix: O(V^2) space
# Adjacency List: O(V+E) space

# Consider a dense graph where each vertex points to each other vertex. 
# Here, the total number of edges will approach V^2. 
# This fact means that regardless of whether you choose an adjacency list or an adjacency matrix, both will have a comparable space complexity. 
# However, dictionaries and sets are less space-efficient than lists. 
# So, for dense graphs (graphs with a high average number of edges per vertex), the adjacency matrix is more efficient because it uses lists instead of dictionaries and sets.

# Takeaway: The worst-case storage of an adjacency list occurs when the graph is dense. The matrix and list representation have the same complexity (O(V^2)). 
# However, for the general case, the list representation is usually more desirable. 
# Also, since finding a vertex's neighbors is a common task, and adjacency lists make this operation more straightforward,
# it is most common to use adjacency lists to represent graphs.

# Add Vertex

# Adjacency Matrix
# Complexity: O(V) time
# For an adjacency matrix, we would need to add a new value to the end of each existing row and add a new row.

# for v in self.edges:
#   self.edges[v].append(0)
# v.append([0] * len(self.edges + 1))

# Note that it's +1 on the last lien, because although you've extended each list, this is getting the len of the whole list of lists
# aka. how many lists there are.
# so will be one less than it is when the new list is added.

# Remember that with Python lists, appending to the end of a list is O(1) because of over-allocation of memory 
# but can be O(n) when the over-allocated memory fills up. When this occurs, adding the vertex can be O(V^2).

# Adjacency List
# Complexity: O(1) time

# self.vertices["H"] = set()
# Adding a new key to a dictionary is a constant-time operation.

# Takeaway: Adding vertices is very inefficient for adjacency matrices but very efficient for adjacency lists.

