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
    def removeDirectedEdge(self, node1, node2):
        node1, node2 = self.getNode(node1), self.getNode(node2)
        node1.removeEdge(node2)
        

    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
       super.getNodes()


if __name__ == "__main__":
    print("Creating Graph...")
    graph = WeightedGraph()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')

    print("Adding Weighted Edge...")
    graph.addWeightedEdge("0", "1", 3)
    graph.printGraph()

    print("\nRemoving an Edge...")
    graph.removeDirectedEdge("0", "1")
    graph.printGraph()

    # graph = Main.createWeightedLinkedList(graph, 10, 2)
    # graph.printGraph()