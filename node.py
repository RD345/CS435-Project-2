# Node class from my Project 1

class Node(object):

    def __init__(self, val):

        self.val = val
        self.connections = [] # Connection format: [(int edge_type), (connected Node node), (int weight)]

    def addEdge(self, connection, connection_type=0):
        self.connections.append([0, connection, connection_type])