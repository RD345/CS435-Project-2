from graph import Graph
import node

class GraphSearch(Graph):
   
    def __init__(self):
        super().__init__()

    # TODO Reveiw
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
        found = DFSHelper(dfs, start_node)
        return dfs


    # TODO Reveiw
    # (e)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> DFSIter(final Node start, final Node end), which iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSIter(self, start_node, end_node):
        stack = visited = []
        found = False
        curr_node = self.getNode(start_node)
        
        curr_node.visited = True # Mark visited
        # visited.append(curr_node)
        stack.append(curr_node)

        while len(stack) > 0: # While there are nodes in the stack
            curr_node = stack.pop(len(stack)-1)
            visited.append(curr_node)
            curr_node.visited = True # Mark visited

            if curr_node.val == str(end_node):
                # curr_node.visited = True # Mark visited
                return visited
            else:
                for neighbor in curr_node.connections:
                    if not neighbor[0].visited:
                        stack.append(neighbor[0])
                        # visited.append(neighbor[0])
                        # curr_node.visited = True # Mark visited
        if found:
            return visited
        else:
            return False


    # TODO Reveiw
    # (f)	(3 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTRec(final Graph graph), which recursively returns an ArrayList of the Nodes in the Graph in a valid Breadth-First Traversal order.
    def BFTRec(self, start_node=0, end_node=1):

        def BFTHelper(bft_arr, curr_node, found=False):
            curr_node.visited = True
            bft_arr.insert(0, curr_node)

            if curr_node.val == str(end_node):
                found = True
            else:
                for neighbor in curr_node.connections:
                    if neighbor and not found and not neighbor[0].visited:
                        bft_arr, found = BFTHelper(bft_arr, neighbor[0], found)

            return bft_arr, found
        
        start_node = self.getNode(start_node)
        bft = []
        found = BFTHelper(bft, start_node)
        # bft = bft.reverse()
        return bft

    # TODO Reveiw
    # (g)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTIter(final Graph graph), which iteratively returns an ArrayList of all of the Nodes in the Graph in a valid Breadth-First Traversal.
    def BFTIter(self, start_node, end_node):
        stack = visited = []
        found = False
        curr_node = self.getNode(start_node)
        
        curr_node.visited = True # Mark visited
        # visited.append(curr_node)
        stack.insert(0, curr_node)

        while len(stack) > 0: # While there are nodes in the stack
            curr_node = stack.pop(len(stack)-1)
            visited.insert(0, curr_node)
            curr_node.visited = True # Mark visited

            if curr_node.val == str(end_node):
                # curr_node.visited = True # Mark visited
                return visited
            else:
                for neighbor in curr_node.connections:
                    if not neighbor[0].visited:
                        stack.insert(0, neighbor[0])
                        # visited.append(neighbor[0])
                        # curr_node.visited = True # Mark visited
        if found:
            return visited
        else:
            return False

    # TODO
    # (h)	(3 points) (You may submit a screenshot for this question, but you’re not required to.) Using the methods above in GraphSearch, in your Main class, implement ArrayList<Node> BFTRecLinkedList(final Graph graph). This should run a BFT recursively on a LinkedList. Your LinkedList should have 10,000 nodes.
    def BFTRecLinkedList(self, graph):
        print()

    # TODO Reveiw
    # (i)	(2 points) Using the methods above in GraphSearch, in your Main class, implement ArrayList<Node> BFTIterLinkedList(final Graph graph). This should run a BFT iteratively on a LinkedList. Your LinkedList should have 10,000 nodes.
    def BFTIterLinkedList(self, n=10000):
        linked_list = GraphSearch.createLinkedList(linked_list, n)
        return linked_list.BFTIter(0, n)

    def printYellow(self, txt): print("\033[93m {}\033[00m" .format(txt)) 

    def printResult(self, arr):
        if arr:
            if arr[0].val == "0":
                for i in range (0, len(arr)):
                    if i is len(arr) - 1:
                        self.printYellow(arr[i].val)
                    else:
                        print(arr[i].val, end='->')
            else:
                for i in reversed(range (0, len(arr))):
                    if i is 0:
                        self.printYellow(arr[i].val)
                    else:
                        print(arr[i].val, end='->')
        else:
            print("\nNo path found")

if __name__ == "__main__":
    print("Creating Graph...")
    graph = GraphSearch()
    graph.addNode('0')
    graph.addNode('1')
    graph.addNode('2')
    graph.printGraph()

    print("Adding Edge...")
    graph.addUndirectedEdge("0", "1")

    print("Doing Traversals...")
    # graph.DFSRec(0, 19)
    # graph.printResult(graph.DFSRec(0, 19))
    # graph.printResult(graph.DFSIter(0, 19))
    graph.printResult(graph.BFTRec(0, 19))
    