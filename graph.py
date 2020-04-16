# Main file
from node import Node
import time

# 3(a)	(5 points) (You must submit code for this question!) Write a class Graph that supports the following methods:
class Graph():
    
    def __init__(self):

        self.nodes = [] # Node list

    
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        self.nodes.append(Node(str(val)))

    # Function to get a Node object. If the target is a node, it will just return it. If the target is a node value, whether it is a string or int, it will search for it and then return the Node object.
    def getNode(self, target):
        if target is Node: # If already a node, return it:
            return target
        elif target is not None: # if target is a string or int, find the node with that value:
            target = str(target)
            try: # Uses the advantage of an array to directly check the index in O(1) time:
                if self.nodes[int(target)].val == target:
                    return self.nodes[int(target)]
            except: # If the index fails, revert to looping through to find the node:
                for node in self.nodes: # Loop through the nodes
                    if node.val == target: # If the current node val is equal to the first node val
                        return node
        else: # Should ideally never be called:
            print(target, "not found")
            return None


    # ii.	void addUndirectedEdge(final Node first, final Node second) - This adds an undirected edge between first and second (and vice versa).
    def addUndirectedEdge(self, node1, node2, weight=None):
        try:
            node1, node2 = self.getNode(node1), self.getNode(node2) # Ensures that input nodes are nodes, and if they are values, it gets the nodes.
            node1.addEdge(node2, 0, weight) # Adds the edge from the first node to the second.
            node2.addEdge(node1, 0, weight) # Adds the edge form the second node to the first.
        except:
            print("An undirected edge creation failed.")


    # Used for certain graph creations, creates a bidirectional edge between two nodes with an optional weight:
    def addBiDirectionalEdge(self, node1, node2, weight=None):
        # try:
        node1, node2 = self.getNode(node1), self.getNode(node2) # Ensures that input nodes are nodes, and if they are values, it gets the nodes.
        node1.addEdge(node2, 2, weight) # Adds the edge from the first node to the second.
        node2.addEdge(node1, 2, weight) # Adds the edge from the second node to the first.
        # except:
        #     print("A bidirectional edge creation failed.")


    # iii.	void removeUndirectedEdge(final Node first, final Node second) - This removes an undirected edge between first and second (and vice versa).
    def removeUndirectedEdge(self, node1, node2):
        try:
            node1, node2 = self.getNode(node1), self.getNode(node2) # Ensures that input nodes are nodes, and if they are values, it gets the nodes.
            node1.removeEdge(node2) # Removes the connection if found.
            node1.removeEdge(node1) # Removes the connection if found.
        except:
            print("An undirected edge removal failed.")


    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
        return set(self.nodes) # Converts to set to eliminate duplicates, if any.
    

    # Print the graph in a very easy to understand way:
    def printGraph(self):
        print('\n' + "Graph:")
        for node in self.nodes:
             print(node.val, end=' ')

        print("\n\nConnections:")
        for node in self.nodes:
            node.printVal()                
            node.printConnections()
        print()

if __name__ == "__main__":
    
    start = time.perf_counter()
    print("Creating Graph...")
    graph = Graph()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')
    graph.addUndirectedEdge("0", "1")
    graph.addBiDirectionalEdge("0", "2")
    graph.printGraph()


    print("\nRemoving an Edge...")
    graph.removeUndirectedEdge("0", "1")
    graph.printGraph()


    # print("\nCreating LinkedList...")
    # graph = Main.createLinkedList(Graph(), 20)
    # graph.printGraph()

    print("Main took:", f"{time.perf_counter()-start:.3}", "seconds") # Prints the time taken for main to run.