from node import Node
from graph import Graph


# (b)	(3 points) (You must submit code for this question!) Write a class WeightedGraph that supports the following methods. You may use similar code as Graph or DirectedGraph above (or better yet, use an Interface to group these classes together).

# TODO
class WeightedGraph(Graph):
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        super().addNode(val)

    # ii.	void addWeightedEdge(final Node first, final Node second, final int edgeWeight) - This adds a directed, weighted edge between first and second (but not vice versa).
    def addWeightedEdge(self, first_node, second_node, weight=0):
        first_node, second_node = self.getNode(first_node), self.getNode(second_node) # Gets the nodes.
        try:
            first_node.addEdge(second_node, 1, weight) # Adds the edge.
        except:
            print("A node could not be found.")

    # iii.	void removeDirectedEdge(final Node first, final Node second) - This removes a directed, weighted edge between first and second (but not vice versa).
    def removeDirectedEdge(self, connection):
        self.connections.getNode(connection)
        connection.removeEdge()


    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
       super.getNodes()

if __name__ == "__main__":
    pass