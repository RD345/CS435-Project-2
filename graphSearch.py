from graph import Graph
import node

class GraphSearch(Graph):
   
    def __init__(self):
        super().__init__()

    # TODO
    # (d)	(3 points) (You must submit code for this question!) In a class called GraphSearch, implement ArrayList<Node> DFSRec(final Node start, final Node end), which recursively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSRec(self, start_node=0, end_node=1):
        
        def DFSHelper(dfs_arr, curr_node, found=False):
            curr_node.visited = True
            dfs_arr.append(curr_node)

            if curr_node.val == str(end_node):
                found = True
            else:
                for neighbor in curr_node.connections:
                    if neighbor and not found and not neighbor[0].visited:
                        dfs_arr, found = DFSHelper(dfs_arr, neighbor[0], found)

            return dfs_arr, found
        
        start_node = self.getNode(start_node)
        dfs = []
        DFSHelper(dfs, start_node)

        # for n in dfs:
        #     if n.val is not end_node:
        #         print(n.val, end='->')
        #     else:
        #         print(n.val)
        
        print()
        return dfs


    # TODO
    # (e)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> DFSIter(final Node start, final Node end), which iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSIter(self, start_node, end_node):
        dfs = []
        found = False
        
        


        if not found:
            return None
        else:
            return dfs

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

    def printResult(self, dfs):
        if dfs[1]:
            for node in dfs:
                print(node.val, end='->')
        else:
            print("\nNo path found")

if __name__ == "__main__":
    # graph = GraphSearch()
    graph = GraphSearch.createRandomUnweightedGraphIter(GraphSearch(), 20)
    graph.printGraph()
    graph.addUndirectedEdge("0", "19")
    # graph.DFSRec(0, 19)
    graph.printResult(graph.DFSRec(0, 19))
    