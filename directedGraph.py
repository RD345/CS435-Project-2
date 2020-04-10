# (b)	 (3 points) (You must submit code for this question!) Write a class DirectedGraph that supports the following methods. You may use similar code as Graph above (or better yet, use an Interface to group these classes together). EDIT: Note: You do not need to worry (yet) about a node only having two neighbors. If you do that here, that's fine, but that's not necessary yet. A node can have as many neighbors as it wants, as long as they're all directed (for example, a node could have an 85-degree forward neighbor, a 70-degree forward neighbor, and a 50-degree forward neighbor or something).
from graph import Graph


class DirectedGraph(Graph):

    def __init__(self):
        super().__init__()

    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        super().addNode(val) # Inherits from Graph.


    # ii.	void addDirectedEdge(final Node first, final Node second) - This adds a directed edge between first and second (but not vice versa).
    def addDirectedEdge(self, first_node, second_node):
        first_node, second_node = self.getNode(first_node), self.getNode(second_node) # Gets the nodes.
        try:
            first_node.addEdge(second_node, 1) # Adds the edge.
        except:
            print("A node could not be found.")

    # iii.	void removeDirectedEdge(final Node first, final Node second) - This removes a directed edge between first and second (but not vice versa).
    def removeDirectedEdge(self, first_node, second_node):
        first_node, second_node = self.getNode(first_node), self.getNode(second_node) # Gets the nodes.
        first_node.removeEdge(second_node)  # Remove the edge


    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getAllNodes(self):
        return self.nodes

if __name__ == "__main__":
    print("Creating directed Graph...")
    graph = DirectedGraph()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')
    graph.addDirectedEdge('0', '1')
    graph.addDirectedEdge('2', '1')
    graph.printGraph()
    graph.removeDirectedEdge('0', '1')
    graph.printGraph()