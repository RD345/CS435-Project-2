from graph import Graph
from node import Node


class GridNode(Node):
    
    def __init__(self, val, x, y):

        self.val = val
        self.x = x
        self.y = y
        self.connections = [] # Connection format: [(connected Node node), (int edge_type 0=undirected, 1=directional, 2=bidirectional), (int weight)]
        self.visited = False


# (a)	(5 points) You must submit code for this question! Write a class GridGraph that supports the following functions: 
class GridGraph(Graph):

    # i.	void addGridNode(final int x, final int y, final String nodeVal) - This adds a new GridNode to the graph with coordinates x and y. A GridNode keeps track of its value as well as its (x,y) coordinates. 
    def addGridNode(self, val, x, y):
        self.nodes.append(GridNode(str(val), x, y))


    # ii.	void addUndirectedEdge(final GridNode first, final GridNode second) - This adds an undirected, unweighted edge between first and second (and vice versa) if first and second are neighbors. If they are not neighbors, do nothing.
    def addUndirectedEdge(self, node1, node2):
        node1, node2 = self.getNode(node1), self.getNode(node2) # Gets the nodes.

        if node1.x == node2.x - 1 or node1.x == node2.x + 1 or node1.x == node2.x: # Checks if nodes are adjacent horizontally. 
            node1.addEdge(node2, 0)
            node2.addEdge(node1, 0)
        elif node1.y == node2.y - 1 or node1.y == node2.y + 1 or node1.y == node2.y: # Checks if nodes are adjacent vetically.  
            node1.addEdge(node2, 0)
            node2.addEdge(node1, 0)


    # iii.	void removeUndirectedEdge(final GridNode first, final GridNode second) - This removes an undirected edge between first and second (and vice versa). 
    def removeUndirectedEdge(self, node1, node2):
        node1, node2 = self.getNode(node1), self.getNode(node2)
        try:
            node1.removeEdge(node2)
            node2.removeEdge(node1)
        except:
            pass


    # iv.	HashSet<GridNode> getAllNodes() - This returns a set of all GridNodes in the graph. 
    def getAllNodes(self):
        return super().getNodes()


if __name__ == "__main__":

    graph = GridGraph()
    graph.addGridNode(0, 0, 0)
    graph.addGridNode(1, 0, 1)
    graph.addUndirectedEdge(0, 1)
    graph.printGraph()

    print("\nRemoving Edge...")
    graph.removeUndirectedEdge(0, 1)
    graph.printGraph()

    print(graph.getAllNodes())