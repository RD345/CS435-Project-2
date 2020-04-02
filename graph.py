# Main file

from node import Node
import random
# Node class from my Project 1

class Graph:
    
    def __init__(self):

        self.visited = False  # If visited
        self.nodes = []       # Node list

    
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        self.nodes.append(Node(str(val)))

    
    # ii.	void addUndirectedEdge(final Node first, final Node second) - This adds an undirected edge between first and second (and vice versa).
    def addUndirectedEdge(self, node1, node2):
        str(node1)
        str(node2)

        for node in self.nodes: # Loop through the nodes
            if node.val == node1: # If the current node val is equal to the first node val
                node1 = node
            elif node.val == node2: # If the current node val is equal to the second node val
                node2 = node

        if node1 is not Node or node2 is str:
            print("A node was not found.")
        else:
            node1.addEdge([node2, 0])
            node2.addEdge([node1, 0])

    
    # iii.	void removeUndirectedEdge(final Node first, final Node second) - This removes an undirected edge between first and second (and vice versa).
    def removeUndirectedEdge(self, node1, node2):
        node1_val = str(node1)
        node2_val = str(node2)

        for node in self.nodes: # Loop through the nodes
            if node.val == node1_val: # If the current node is equal to the first node
                node1 = node
                for conn in node1.connections: # Loop thorough the connections in the first node
                    if conn[0] == node2:
                        node1.connections.remove(conn)
            elif node.val == node2_val: # If the current node is equal to the second node
                node2 = node
                for conn in node2.connections: # Loop thorough the connections in the first node
                    if conn[0] == node1:
                        node1.connections.remove(conn)

        if node1 == str or node2 == str:
            print("A node was not found.")
            return
        

    def addBiDirectionalEdge(self, node1, node2, weight=None):
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

        node1.connections.append([node2, 2, weight])
        node2.connections.append([node1, 2, weight])


    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
        return self.nodes

    # (b)	(2 points) (You must submit code for this question!) In your Main class, create a nonrecursive method called Graph createRandomUnweightedGraphIter(int n) that creates n random nodes with randomly assigned unweighted, bidirectional edges. You should use some of the methods you implemented in part (a). Make sure you’re either implementing an adjacency list or an adjacency matrix to keep track of your edges!
    def createRandomUnweightedGraphIter(self, n=10):
        graph = Graph()
        
        for i in range(0, n):
            graph.addNode(i)

        for i in range(0, n):
            node1 = graph.nodes[i]
            node2 = random.choice(graph.nodes)
            graph.addBiDirectionalEdge(node1, node2)
        return graph


    # (c)	(2 points) (You must submit code for this question!) In your Main class, create a non-recursive method called Graph createLinkedList(int n) that creates a Graph with n nodes where each node only has an edge to the next node created. For example, if you create nodes 1, 2, and 3, Node 1 only has an edge to Node 2, and Node 2 only has an edge to Node 3.
    def createLinkedList(self, n=10):
        graph = Graph()

        for i in range(0, n):
            graph.addNode(i)
            if i > 0:
                graph.nodes[i-1].connections.append([graph.nodes[i], 1, None])
            prev_node = graph.nodes[i]
        
        return graph


    def printGraph(self):
        print('\n' + "Graph:")
        for node in self.nodes:
             print(node.val, end=' ')

        print("\nConnections:")
        for node in self.nodes:
            for conn in node.connections:
                # print(conn, end=' ')

                if conn[1] == 0: # If type is undirectional
                    print(node.val, '---', conn[0].val)
                    if conn[2] is not None:
                        print("W:", conn[2])
                    
                elif conn[1] == 1: # If type is directional
                    print(node.val, '-->', conn[0].val)
                    if conn[2] is not None:
                        print("W:", conn[2])

                elif conn[1] == 2: # If type is bidirectional
                    if int(conn[0].val) > int(node.val):
                        print(node.val, '<->', conn[0].val)
                        if conn[2] is not None:
                            print("W:", conn[2])
            

if __name__ == "__main__":
    
    print("Creating Random Unweighted Graph...")
    graph = Graph()
    graph = graph.createRandomUnweightedGraphIter(20)
    graph.addUndirectedEdge("0", "1")
    graph.printGraph()

    print("\nRemoving an Edge...")
    graph.removeUndirectedEdge("0", "1")
    graph.printGraph()

    print("\nCreating LinkedList...")
    graph = graph.createLinkedList(20)
    graph.printGraph()