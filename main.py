from node import Node
from graph import Graph
from graphSearch import GraphSearch
from directedGraph import DirectedGraph
import random


# (c)	(3 points) (You must submit code for this question!) In your Main class, create a non-recursive method called DirectedGraph createRandomDAGIter(final int n) that creates n random nodes with randomly assigned unweighted, directed edges. You should use some of the methods you implemented in part (a) of this question. Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges, and keeping track of directionality!
# TODO
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

if __name__ == "__main__":
    
    dir_graph = createRandomDAGIter(DirectedGraph(), 10)
    dir_graph.printGraph()