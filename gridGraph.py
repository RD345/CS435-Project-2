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

    def __init__(self):

        self.nodes = [[]] # Node list

    # i.	void addGridNode(final int x, final int y, final String nodeVal) - This adds a new GridNode to the graph with coordinates x and y. A GridNode keeps track of its value as well as its (x,y) coordinates. 
    def addGridNode(self, val, x, y):
        try:
            self.nodes[x].append(GridNode(str(val), x, y))
        except IndexError:
            self.nodes.append([])
            self.nodes[x].append(GridNode(str(val), x, y))


    # ii.	void addUndirectedEdge(final GridNode first, final GridNode second) - This adds an undirected, unweighted edge between first and second (and vice versa) if first and second are neighbors. If they are not neighbors, do nothing.
    def addUndirectedEdge(self, node1, node2):
        node1, node2 = self.getNode(node1), self.getNode(node2) # Gets the nodes.
        if node1 == None or node2 == None:
            print("Node is none.")
            return
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
        nodes = set()
        for row in self.nodes: # Loop through the rows
            for node in row:
                nodes.add(node)
        return nodes


    # Function to get a Node object. If the target is a node, it will just return it. If the target is a node value, whether it is a string or int, it will search for it and then return the Node object.
    def getNode(self, target):
        if target is GridNode: # If already a GridNode, return it:
            return target
        elif target is not None: # if target is a string or int, find the node with that value:
            target = str(target)
            try: # Uses the advantage of an array to directly check the index in O(1) time:
                for row in self.nodes: # Loop through the rows
                    for node in row:
                        if str(node.val) == target:
                            return node
            except: # If the index fails, revert to looping through to find the node:
                for row in self.nodes: # Loop through the rows
                    for node in row:
                        if node.val == target: # If the current node val is equal to the first node val
                            return node
        else: # Should ideally never be called:
            print(target, "not found")
            return None


    def printGraph(self):
        print('\n' + "Graph:")
        for row in self.nodes:
            for node in row:
                print(node.val, end=' ')


        print("\nConnections:")
        for row in self.nodes:
            for node in row:
                print(node.val, ' ', '[', node.x, ',', node.y, ']', sep='', end=' ')
                
                node.printConnections()
                print()

        print()


if __name__ == "__main__":

    graph = GridGraph()
    graph.addGridNode(0, 0, 0)
    graph.addGridNode(1, 0, 1)
    graph.addUndirectedEdge(0, 1)
    graph.addUndirectedEdge(0, 1)
    graph.printGraph()
    print(graph.getNode(1).val)

    print("\nRemoving Edge...")
    graph.removeUndirectedEdge(0, 1)
    graph.printGraph()

    print(graph.getAllNodes())