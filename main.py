from node import Node
from graph import Graph
from graphSearch import GraphSearch
from directedGraph import DirectedGraph
from weightedGraph import WeightedGraph
import random


# (c)	(3 points) (You must submit code for this question!) In your Main class, create a non-recursive method called DirectedGraph createRandomDAGIter(final int n) that creates n random nodes with randomly assigned unweighted, directed edges. You should use some of the methods you implemented in part (a) of this question. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges, and keeping track of directionality!
def createRandomDAGIter(self, node_count=10):
    # Create the nodes:
    for n in range(node_count):
        self.addNode(n)

    for node in self.nodes:
        connect = node
        while connect is node: # Keeps going if it tries to connect to itself.
            connect = random.choice(self.nodes)

        self.addDirectedEdge(node.val, connect.val)
    
    return self

# (c)	(4 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called WeightedGraph createRandomCompleteWeightedGraph(final int n). This should make a complete weighted graph, which means that each node has a randomly weighted positive integer edge to every other edge in the graph. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your weighted edges, and keeping track of directionality! EDIT: You should have a total of n (n1) directed edges, each with a random edge weight to each other node.
# TODO Needs connections between every node
def createRandomCompleteWeightedGraph(self, node_count=10):
    for n in range(node_count):
        self.addNode(n)

    for node in self.nodes:
        connect = node
        while connect is node: # Keeps going if it tries to connect to itself.
            connect = random.choice(self.nodes)

        self.addWeightedEdge(node.val, connect.val, random.randrange(0, node_count/5))
    
    return self


def createWeightedLinkedList(self, node_count):
    pass

if __name__ == "__main__":
    
    dir_graph = createRandomDAGIter(DirectedGraph())
    dir_graph.printGraph()

    weighted_graph = createRandomCompleteWeightedGraph(WeightedGraph())
    weighted_graph.printGraph()