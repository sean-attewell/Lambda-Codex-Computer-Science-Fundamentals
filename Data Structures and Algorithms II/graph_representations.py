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

class Graph_Adjacency_List_with_weights:
    def __init__(self):
        self.vertices = {
                            "A": {"B": 1},
                            "B": {"C": 3, "D": 2},
                            "C": {},
                            "D": {},
                            "E": {"D": 1}
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

# Note that it's +1 on the last line, because although you've extended each list, this is getting the len of the whole list of lists
# aka. how many lists there are (one less than when the new list is added).

# Remember that with Python lists, appending to the end of a list is O(1) because of over-allocation of memory 
# but can be O(n) when the over-allocated memory fills up (if you exceed the current size of the array, it needs to make a new bigger array and copy everything over). 
# When this occurs, adding the vertex can be O(V^2), because you're doing it for every list.

# Adjacency List
# Complexity: O(1) time

# self.vertices["H"] = set()
# Adding a new key to a dictionary is a constant-time operation.

# Takeaway: Adding vertices is very inefficient for adjacency matrices but very efficient for adjacency lists.

# Remove Vertex
# Removing vertices is inefficient in both representations, but faster in lists than matrix. 

# Adjacency Matrix
# Complexity: O(V^2)

# In an adjacency matrix, we need to remove the removed vertex's row and then remove that column from each row. 
# Removing an element from a list requires moving everything after that element over by one slot, which takes an average of V/2 operations. 
# Since we need to do that for every single row in our matrix, that results in V^2 time complexity. 
# We need to reduce each vertex index after our removed index by one as well, which doesn't add to our quadratic time complexity but adds extra operations.

# Adjacency List
# Complexity: O(V)

# We need to visit each vertex for an adjacency list and remove all edges pointing to our removed vertex. 
# Removing elements from sets and dictionaries is an O(1) operation, resulting in an overall O(V) time complexity.

# Takeaway: Removing vertices is inefficient in both adjacency matrices and lists but more efficient in lists.

# Add Edge
# Adjacency Matrix
# Complexity: O(1)

# Adding an edge in an adjacency matrix is simple:

# self.edges[v1][v2] = 1
# Adjacency List
# Complexity: O(1)

# Adding an edge in an adjacency list is simple:

# self.vertices[v1].add(v2)
# Both are constant-time operations.

# Takeaway: Adding edges to both adjacency matrices and lists is very efficient.

# Remove Edge
# Adjacency Matrix
# Complexity: O(1)

# Removing an edge from an adjacency matrix is simple:

# self.edges[v1][v2] = 0

# Adjacency List
# Complexity: O(1)

# Removing an edge from an adjacency list is simple:

# self.vertices[v1].remove(v2)

# Both are constant-time operations.
# Takeaway: Removing edges from both adjacency matrices and lists is very efficient.


# Find Edge

# Adjacency Matrix
# Complexity: O(1)

# Finding an edge in an adjacency matrix is simple:

# return self.edges[v1][v2] > 0

# Adjacency List
# Complexity: O(1)

# Finding an edge in an adjacency list is simple:

# return v2 in self.vertices[v1]
# Both are constant-time operations.

# Takeaway: Finding edges in both adjacency matrices and lists is very efficient.

# Get All Edges from Vertex
# You can use several commands if you want to know all the edges originating from a particular vertex.

# Adjacency Matrix
# Complexity: O(V)

# In an adjacency matrix, this is complicated. You would need to iterate through the entire row and populate a list based on the results:

# v_edges = []
# for v2 in self.edges[v]:
#     if self.edges[v][v2] > 0:
#         v_edges.append(v2)
# return v_edges


# Adjacency List
# Complexity: O(1)

# With an adjacency list, this is as simple as returning the value from the vertex dictionary:

# return self.vertex[v]

# Takeaway: Fetching all edges is less efficient in an adjacency matrix than an adjacency list.

# In most practical use-cases, an adjacency list will be a better choice for representing a graph. 
# However, it is also crucial that you be familiar with the matrix representation. Why? 
# Because there are some dense graphs or weighted graphs that could have better space efficiency when represented by a matrix.

