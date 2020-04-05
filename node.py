# Node class from my Project 1

class Node(object):

    def __init__(self, val):

        self.val = val
        self.connections = [] # Connection format: [(connected Node node), (int edge_type 0=undirected, 1=directional, 2=bidirectional), (int weight)]
        self.visited = False

    def addEdge(self, connected_node, connection_type=0, weight=None):
        self.connections.append([connected_node, connection_type, weight])