# Node class

class Node(object):

    def __init__(self, val):

        self.val = val
        self.connections = [] # Connection format: [(connected Node node), (int edge_type 0=undirected, 1=directional, 2=bidirectional), (int weight)]
        self.visited = False

    # Add an edge:
    def addEdge(self, connected_node, connection_type=0, weight=None):
        duplicate = False
        for conn in self.connections:
            if conn[0] == connected_node:
                duplicate = True

        if not duplicate:        
            self.connections.append([connected_node, connection_type, weight])

    # Remove and edge:
    def removeEdge(self, connected_node):
        for conn in self.connections: # Loop thorough the connections in the node
            if conn[0] == connected_node: 
                self.connections.remove(conn)


    def printConnections(self):
        for conn in self.connections: # Loop thorough the connections in the node
            if conn[1] == 0: # If type is undirectional
                    print('(', '--- ', conn[0].val, ')', end=' ', sep='')
            elif conn[1] == 1: # If type is directional
                print('(', '--> ', conn[0].val, ')', end=' ', sep='')
            elif conn[1] == 2: # If type is bidirectional
                print('(', '<-> ', conn[0].val, ')', end=' ', sep='')
                
            if conn[2] is not None:
                print("[W:", str(conn[2]) + ']', end='')


    def printVal(self):
        if int(self.val) < 10:
            print('\n  ', self.val, ':', end=' ', sep='')
        elif int(self.val) < 100:
            print('\n ', self.val, ':', end=' ', sep='')
        else:
            print('\n', self.val, ':', end=' ', sep='')


    # Reset the visited value:
    def resetVisted(self):
        self.visited = False

    