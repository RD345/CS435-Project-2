# Node class

class Node(object):

    def __init__(self, val):

        self.val = val
        self.connections = [] # Connection format: [(connected Node node), (int edge_type 0=undirected, 1=directional, 2=bidirectional), (int weight)]
        self.visited = False

    # Add an edge:
    def addEdge(self, connected_node, connection_type=0, weight=None):
        self.connections.append([connected_node, connection_type, weight])

    # Remove and edge:
    def removeEdge(self, connected_node):
        for conn in self.connections: # Loop thorough the connections in the node
            if conn[0] == connected_node: 
                self.connections.remove(conn)


    # Reset the visited value:
    def resetVisted(self):
        self.visited = False

    