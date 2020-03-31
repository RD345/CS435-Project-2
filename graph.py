# Main file
import node as Node

class Graph:

    def __init__(self):
        self.visited
        self.connetions

    # TODO
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self):
        print(Node.insertIter())

    # TODO
    # ii.	void addUndirectedEdge(final Node first, final Node second) - This adds an undirected edge between first and second (and vice versa).
    def addUndirectedEdge(self):
        print()

    # TODO
    # iii.	void removeUndirectedEdge(final Node first, final Node second) - This removes an undirected edge between first and second (and vice versa).
    def removeUndirectedEdge(self, node1, node2):
        print()

    # TODO
    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
        print()

    # TODO
    # (b)	(2 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called Graph createRandomUnweightedGraphIter(int n) that creates n random nodes with randomly assigned unweighted, bidirectional edges. You should use some of the methods you implemented in part (a). Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges!
    def createRandomUnweightedGraphIter(self, n):
        print()

    # TODO
    # (c)	(2 points) (You must submit code for this question!) In your Main class, create a non-recursive method called Graph createLinkedList(int n) that creates a Graph with n nodes where each node only has an edge to the next node created. For example, if you create nodes 1, 2, and 3, Node 1 only has an edge to Node 2, and Node 2 only has an edge to Node 3.
    def createLinkedList(self, n):
        print()
   

class graphSearch:

    # TODO
    # (d)	(3 points) (You must submit code for this question!) In a class called GraphSearch, implement ArrayList<Node> DFSRec(final Node start, final Node end), which recursively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSRec(self, start_node, end_node):
        print()

    # TODO
    # (e)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> DFSIter(final Node start, final Node end), which iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSIter(self, start_node, end_node):
        print()

    # TODO
    # (f)	(3 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTRec(final Graph graph), which recursively returns an ArrayList of the Nodes in the Graph in a valid Breadth-First Traversal order.
    def BFTRec(self, graph):
        print()

    # TODO
    # (g)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTIter(final Graph graph), which iteratively returns an ArrayList of all of the Nodes in the Graph in a valid Breadth-First Traversal.
    def BFTIter(self, graph):
        print()

    # TODO
    # (h)	(3 points) (You may submit a screenshot for this question, but you’re not required to.) Using the methods above in GraphSearch, in your Main class, implement ArrayList<Node> BFTRecLinkedList(final Graph graph). This should run a BFT recursively on a LinkedList. Your LinkedList should have 10,000 nodes.
    def BFTRecLinkedList(self, graph):
        print()

    # TODO
    # (i)	(2 points) Using the methods above in GraphSearch, in your Main class, implement ArrayList<Node> BFTIterLinkedList(final Graph graph). This should run a BFT iteratively on a LinkedList. Your LinkedList should have 10,000 nodes.
    def BFTIterLinkedList(self, graph):
        print()


if __name__ == "__main__":
    print("test")