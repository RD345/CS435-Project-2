from graph import Graph


class GraphSearch(Graph):
   
    def __init__(self):
        super().__init__()


    # 3(d)	(3 points) (You must submit code for this question!) In a class called GraphSearch, implement ArrayList<Node> DFSRec(final Node start, final Node end), which recursively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSRec(self, start_node=0, end_node=1):
        
        def DFSHelper(dfs_arr, curr_node, found=False):
            curr_node.visited = True
            dfs_arr.append(curr_node)

            if curr_node.val == str(end_node): #  Checks if the string value of the node is equal to the stringified end_node. 
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


    # 3(e)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> DFSIter(final Node start, final Node end), which iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFSIter(self, start_node, end_node):
        stack, visited = [], []
        found = False
        curr_node = self.getNode(start_node) # Ensures that start_node is a Node object.
        
        curr_node.visited = True # Mark current node visited.
        stack.append(curr_node) # Stacks the node.

        while len(stack) > 0: # While there are nodes in the stack
            curr_node = stack.pop() # Pops the top node and makes it the current one.
            visited.append(curr_node) # Add it to the visited list.
            curr_node.visited = True # Marks the node visited

            if curr_node.val == str(end_node):
                return visited
            else:
                for neighbor in curr_node.connections: # Loops through the neighbors:
                    if not neighbor[0].visited:
                        stack.append(neighbor[0]) # Stacks the unvisited neighbors.
                       
        if found: # If the end_node was found, return the visited list:
            return visited
        else: # Otherwise return False:
            return False


    # 3(f)	(3 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTRec(final Graph graph), which recursively returns an ArrayList of the Nodes in the Graph in a valid Breadth-First Traversal order.
    def BFTRec(self, start_node=0, end_node=1):

        def BFTHelper(visited, curr_node, found=False):
            curr_node.visited = True
            visited.append(curr_node)
           
            if curr_node.val == end_node:
                return visited, True
            else:
                for neighbor in curr_node.connections:
                    if neighbor and not found and not neighbor[0].visited:
                        visited, found = BFTHelper(visited, neighbor[0], found)

            return visited, found
        
        start_node, end_node = self.getNode(start_node), str(end_node)
        bft = []
        BFTHelper(bft, start_node)
        return bft


    # 3(g)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTIter(final Graph graph), which iteratively returns an ArrayList of all of the Nodes in the Graph in a valid Breadth-First Traversal.
    def BFTIter(self, start_node, end_node):
        queue, visited = [], []
        curr_node = self.getNode(start_node)
        end_node = str(end_node)
        
        curr_node.visited = True # Mark visited
        # visited.append(curr_node)
        queue.append(curr_node)

        # While there are nodes in the queue:
        while len(queue) > 0: 
            curr_node = queue.pop(0) # Gets the first node in the queue
            curr_node.visited = True # Marks the node as visited
            visited.append(curr_node) # Adds it to the visited list
            # print(curr_node.val)

            if curr_node.val == end_node:
                return visited
            else:
                for connection in curr_node.connections:
                    neighbor = connection[0]
                    if not neighbor.visited:
                        queue.append(neighbor)
                        # visited.append(neighbor[0])
                        # curr_node.visited = True # Mark visited
       
        return False


    def printYellow(self, txt): print("\033[93m {}\033[00m" .format(txt)) 

    def printResult(self, union):
        if union:
            for i in range (len(union)-1):
                print(union[i].val, end='->')

            GraphSearch.printYellow(GraphSearch(), union[len(union)-1].val)
            
            # for i in reversed(range (0, len(union))):
            #     if i is 0:
            #         self.printYellow(union[i].val)
            #     else:
            #         print(union[i].val, end='->')
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
    graph.addUndirectedEdge("1", "2")

    print("Doing Traversals...")
    # graph.DFSRec(0, 19)
    # Only one will work at a time due to visiting not being reset:
    graph.printResult(graph.DFSRec(0, 2))
    graph.printResult(graph.DFSIter(0, 2))
    # graph.printResult(graph.BFTRec(0, 2)) 
    # graph.printResult(graph.BFTIter(0, 2))
    