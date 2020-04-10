# Main file
from node import Node

# 3(a)	(5 points) (You must submit code for this question!) Write a class Graph that supports the following methods:
class Graph():
    
    def __init__(self):

        self.nodes = [] # Node list

    
    # i.	void addNode(final String nodeVal) - This adds a new node to the graph.
    def addNode(self, val):
        self.nodes.append(Node(str(val)))

    def getNode(self, target):
        if target is Node:
            return target
        elif target is str:
            for node in self.nodes: # Loop through the nodes
                if node.val == target: # If the current node val is equal to the first node val
                    return node
        elif target is not None:
            target = str(target)
            for node in self.nodes: # Loop through the nodes
                if node.val == target: # If the current node val is equal to the first node val
                    return node
        else:
            print(target, "not found")
            return None


    # ii.	void addUndirectedEdge(final Node first, final Node second) - This adds an undirected edge between first and second (and vice versa).
    def addUndirectedEdge(self, node1, node2, weight=None):
        node1, node2 = self.getNode(node1), self.getNode(node2)
        
        node1.addEdge(node2, 0, weight)
        node2.addEdge(node1, 0, weight)

    
    # iii.	void removeUndirectedEdge(final Node first, final Node second) - This removes an undirected edge between first and second (and vice versa).
    def removeUndirectedEdge(self, node1, node2):
        node1, node2 = self.getNode(node1), self.getNode(node2)

        for conn in node1.connections: # Loop thorough the connections in the first node
            if conn[0] == node2:
                node1.removeEdge(conn)

        for conn in node2.connections: # Loop thorough the connections in the first node
            if conn[0] == node1:
                node1.removeEdge(conn)
        
    # iv.	HashSet<Node> getAllNodes() - This returns a set of all Nodes in the graph.
    def getNodes(self):
        return self.nodes

    # Unused in this class, creates a bidirectional edged between two nodes:
    def addBiDirectionalEdge(self, node1, node2, weight=None):
        if node1 == None or node2 == None:
            print("Edge Creation failed")
            return

        node1.connections.append([node2, 2, weight])
        node2.connections.append([node1, 2, weight])
    

    def printGraph(self):
        print('\n' + "Graph:")
        for node in self.nodes:
             print(node.val, end=' ')

        print("\n\nConnections:")
        for node in self.nodes:
            if int(node.val) < 10:
                print('\n  ', node.val, ':', end=' ', sep='')
            elif int(node.val) < 100:
                print('\n ', node.val, ':', end=' ', sep='')
            else:
                print('\n', node.val, ':', end=' ', sep='')
                
            for conn in node.connections:
                if conn[1] == 0: # If type is undirectional
                    print('(', '--- ', conn[0].val, ')', end=' ', sep='')
                elif conn[1] == 1: # If type is directional
                    print('(', '--> ', conn[0].val, ')', end=' ', sep='')
                elif conn[1] == 2: # If type is bidirectional
                    print('(', '<-> ', conn[0].val, ')', end=' ', sep='')
                
                if conn[2] is not None:
                    print("[W:", str(conn[2]) + ']', end='')
        print()

if __name__ == "__main__":
    
    print("Creating Graph...")
    graph = Graph()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')
    graph.addUndirectedEdge("0", "1")
    graph.printGraph()


    print("\nRemoving an Edge...")
    graph.removeUndirectedEdge("0", "1")
    graph.printGraph()

    # print("\nCreating LinkedList...")
    # graph = Main.createLinkedList(Graph(), 20)
    # graph.printGraph()