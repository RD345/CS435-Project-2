# Main file

from node import Node
import random
# Node class from my Project 1

class Graph:
    
    def __init__(self):

        self.visited = False  # If visited
        self.nodes = []       # Node list
        self.connections = [] # Connection matrix

    
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        self.nodes.append(Node(str(val)))

    
    # ii.	void addUndirectedEdge(final Node first, final Node second) - This adds an undirected edge between first and second (and vice versa).
    def addUndirectedEdge(self, node1, node2):
        self.connections.append([0, node1, node2, 0]) # 0 is undirected
        node1_val = str(node1)
        node2_val = str(node2)

        for node in self.nodes: # Loop through the nodes
            if node.val == node1_val: # If the current node is equal to the first node
                node1 = node
            elif node.val == node2_val: # If the current node is equal to the second node
                node2 = node

        if node1 == str or node2 == str:
            print("A node was not found.")
            return

        for conn in node1.connections: # Loop thorough the connections in the first node
            if conn[1] == node2:
                node1.connections.remove[node2]

        for conn in node2.connections: # Loop thorough the connections in the first node
            if conn[1] == node2:
                node1.connections.remove[node2]

        self.nodes[int(node1.val)].addEdge(self.nodes[int(node2.val)])

    
    # iii.	void removeUndirectedEdge(final Node first, final Node second) - This removes an undirected edge between first and second (and vice versa).
    def removeUndirectedEdge(self, node1, node2):
        node1_val = str(node1)
        node2_val = str(node2)

        for node in self.nodes: # Loop through the nodes
            if node.val == node1_val: # If the current node is equal to the first node
                node1 = node
            elif node.val == node2_val: # If the current node is equal to the second node
                node2 = node

        if node1 == str or node2 == str:
            print("A node was not found.")
            return

        for conn in node1.connections: # Loop thorough the connections in the first node
            if conn[1] == node2:
                node1.connections.remove(conn)

        for conn in node2.connections: # Loop thorough the connections in the first node
            if conn[1] == node1:
                node1.connections.remove(conn)


    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
        return self.nodes

    # (b)	(2 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called Graph createRandomUnweightedGraphIter(int n) that creates n random nodes with randomly assigned unweighted, bidirectional edges. You should use some of the methods you implemented in part (a). Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges!
    def createRandomUnweightedGraphIter(n):
        graph = Graph()
        arr = []
        for i in range(0, n):
            graph.addNode(str(i))
            arr.append(str(i))

        node1 = str(random.choice(arr))
        arr.remove(node1)
        node2 = str(random.choice(arr))
        arr.remove(node2)

        graph.addUndirectedEdge(node1, node2)
        return graph


    # (c)	(2 points) (You must submit code for this question!) In your Main class, create a non-recursive method called Graph createLinkedList(int n) that creates a Graph with n nodes where each node only has an edge to the next node created. For example, if you create nodes 1, 2, and 3, Node 1 only has an edge to Node 2, and Node 2 only has an edge to Node 3.
    def createLinkedList(n):
        graph = Graph()
        prev_node = None

        for i in range(0, n):
            graph.addNode(str(i))
            if prev_node:
                graph.addUndirectedEdge(prev_node, str(i))
            prev_node = str(i)
        
        return graph

    def printGraph(self):
        print('\n' + "Connections:")
        for node in self.nodes:
            for conn in node.connections:
                # print(conn, end=' ')

                if conn[0] == 0:
                    print(node.val, '--', conn[1].val, end='')
                    if conn[2] > 0:
                        print("W:", conn[2])
                    else:
                        print()
                elif conn[0] == 1:
                    print(node.val, '->', conn[1].val, "W:", conn[2])
                    if conn[2] > 0:
                        print("W:", conn[2])
                    else:
                        print()

if __name__ == "__main__":
    
    graph = Graph.createRandomUnweightedGraphIter(20)

    # graph.addNode("1")
    graph.addUndirectedEdge("0", "1")
    print(graph.printGraph())
    graph.removeUndirectedEdge("0", "1")

    print(graph.printGraph())

    graph = Graph.createLinkedList(20)
    print(graph.printGraph())