from node import Node
from graph import Graph
from graphSearch import GraphSearch
from directedGraph import DirectedGraph
from weightedGraph import WeightedGraph
from gridGraph import GridGraph
import random, math



# 3(b)	(2 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called Graph createRandomUnweightedGraphIter(int n) that creates n random nodes with randomly assigned unweighted, bidirectional edges. You should use some of the methods you implemented in part (a). Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges!
def createRandomUnweightedGraphIter(self, n=10): 
    self = Graph()       
    for i in range(n):
        self.addNode(i)

    for node in self.nodes:
        connect = node
        while connect is node:
            connect = random.choice(self.nodes)
        self.addBiDirectionalEdge(node, connect)
    return self


# 3(c)	(2 points) (You must submit code for this question!) In your Main class, create a non-recursive method called Graph createLinkedList(int n) that creates a Graph with n nodes where each node only has an edge to the next node created. For example, if you create nodes 1, 2, and 3, Node 1 only has an edge to Node 2, and Node 2 only has an edge to Node 3.
def createLinkedList(self, n=10):
    self = Graph()

    for i in range(0, n):
        self.addNode(i)
        if i > 0:
            self.nodes[i-1].addEdge(self.nodes[i], 1)
        prev_node = self.nodes[i]
    
    return self


# 4(c)	(3 points) (You must submit code for this question!) In your Main class, create a non-recursive method called DirectedGraph createRandomDAGIter(final int n) that creates n random nodes with randomly assigned unweighted, directed edges. You should use some of the methods you implemented in part (a) of this question. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges, and keeping track of directionality!
def createRandomDAGIter(self, node_count=10):
    self = DirectedGraph()
    # Create the nodes:
    for n in range(node_count):
        self.addNode(n)

    for node in self.nodes:
        connect = node
        while connect is node: # Keeps going if it tries to connect to itself.
            connect = random.choice(self.nodes)

        self.addDirectedEdge(node.val, connect.val)
    
    return self

# 5(c)	(4 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called WeightedGraph createRandomCompleteWeightedGraph(final int n). This should make a complete weighted graph, which means that each node has a randomly weighted positive integer edge to every other edge in the graph. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your weighted edges, and keeping track of directionality! EDIT: You should have a total of n (n1) directed edges, each with a random edge weight to each other node.
def createRandomCompleteWeightedGraph(self, node_count=10):
    self = WeightedGraph()

    for n in range(node_count):
        self.addNode(n)

    for node in self.nodes:
        # Connect to every other node:
        for connect in self.nodes: 
            if node is not connect: # If not self
                self.addWeightedEdge(node.val, connect.val, random.randrange(0, int(node_count/3))) # Creates edge with random weight in between 0 and one third the number of nodes
    
    return self

# 5(d)	(2 points) (You must submit code for this question!) In your Main class, create a non-recursive method called WeightedGraph createLinkedList(final int n). This should make a weighted graph with n nodes, each having a single edge to the next node of uniform weight (perhaps weight 1). This can look very similar to the method you implemented in part 3c. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges, and keeping track of directionality!
def createWeightedLinkedList(self, node_count=10, weight=1):
    self = WeightedGraph()

    for i in range(node_count):
        self.addNode(i)
        if i > 0:
            self.nodes[i-1].addEdge(self.nodes[i], 1, weight)
        prev_node = self.nodes[i]
    
    return self


# 5(e)	(10 points) (You must submit code for this question!) EDIT: Changed this to add it to your Main class. In a class called TreadmillMazeSolver, implement HashMap<Node, Integer> Dijkstra’s(final Node start). This should return a dictionary mapping each Node in the graph to the minimum value from start to get to node.
# EDIT: This should NOT use Graph as an input! The only exception to this if you need your Graph instance to call some API like getNeighborNodes(final Node node). Other than this, you should not be using a Graph parameter for anything else.
# TODO
def Dijkstras():
    pass

# 6(b) (5 points) (You must submit code for this question!) In your Main class, create a non-recursive method called GridGraph createRandomGridGraph(int n) that creates n2 random nodes with randomly assigned unweighted, bidirectional edges. These nodes should be (0,0), (1,0), (2,0),..., (n,0),(0,1),(1,1),...(n,1),...,(n,n). Nodes should have a 50% chance of being connected to their neighbors, and a 0% chance of being connected to non-neighbors. For example, the Node at (1,1) should have a 50% chance of being connected to the node (0,1), 50% to (1,0), 50% to (2,1), and 50% to (1,2), but a 0% chance of being connected to (2,2). 
def createRandomGridGraph(self, node_count_sq=10):
    self = GridGraph()
    rows = cols = node_count_sq

    for row in range(rows):
        for col in range(cols):
            self.addGridNode(str(row*node_count_sq + col), row, col)

    for row in self.nodes:
        for node in row:
            if random.randint(0, 9) >= 7 and node.y > 0: # If left node, connects 50%(~49%) of the time
                self.addBiDirectionalEdge(node, self.nodes[node.x][node.y - 1])

            if random.randint(0, 9) >= 7 and node.y < node_count_sq - 1: # If right node, connects 50%(~49%) of the time
                self.addBiDirectionalEdge(node, self.nodes[node.x][node.y + 1])

            if random.randint(0, 9) >= 7 and node.x > 0: # If top node, connects 50%(~49%) of the time
                self.addBiDirectionalEdge(node, self.nodes[node.x - 1][node.y])

            if random.randint(0, 9) >= 7 and node.x < node_count_sq - 1: # If bottom node, connects 50%(~49%) of the time
                self.addBiDirectionalEdge(node, self.nodes[node.x  + 1][node.y])

    return self

# (d) (10 points) (You must submit code for this question!) In Main, call createRandomGridGraph(100) and store sourceNode as the node at (0,0) and destNode as the node at (100,100). implement ArrayList<Node> astar(final sourceNode, final destNode). Ensure that you are using the heuristic you established in part (e). This should return an ordered list, from sourceNode and ending at destNode.
def aStar(self, start, end):
    pass

# Completion status:
# 3 Complete: a, b, c, ~d, ~e, ~f, ~g, ~i | Incomplete: h
# 4 Complete: b, c,                       | Incomplete: d, e
# 5 Complete: b, c, d,                    | Incomplete: e
# 6 Complete: a, b                        | Incomplete: c, d
# 7 Complete:                             | Incomplete: a
if __name__ == "__main__":
    # Graph:
    graph = Graph()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')
    graph.addNode('3')
    createLinkedList(graph)

    # Directed Graph:
    dir_graph = createRandomDAGIter(DirectedGraph())
    dir_graph.printGraph()

    # Weighted Graph:
    weighted_graph = WeightedGraph()
    weighted_graph = createRandomCompleteWeightedGraph(WeightedGraph(), 10)
    weighted_graph.printGraph()

    # Weighted Linked List:
    wll = createWeightedLinkedList(graph, 10, 2)
    wll.printGraph()

    # graph = GraphSearch()
    graph = createRandomUnweightedGraphIter(GraphSearch(), 20)
    graph.printGraph()
    # graph.addUndirectedEdge("0", "19")
    # graph.DFSRec(0, 19)
    # graph.printResult(graph.DFSRec(0, 19))
    # graph.printResult(graph.DFSIter(0, 19))
    # GraphSearch.printYellow("Test")
    # graph.printResult(graph.BFTRec(0, 19))

    gGraph = createRandomGridGraph(GridGraph(), 8)
    gGraph.printGraph()
