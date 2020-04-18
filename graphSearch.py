from graph import Graph


class GraphSearch(Graph):
   
    def __init__(self):

        super().__init__()


    # 3(d)	(3 points) (You must submit code for this question!) In a class called GraphSearch, implement ArrayList<Node> DFTRec(final Node start, final Node end), which recursively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFTRec(self, start_node=0):
        
        def __DFSHelper(dft_arr, curr_node):
            curr_node.visited = True
            dft_arr.append(curr_node)
            
            for neighbor in curr_node.connections:
                if neighbor and not neighbor[0].visited:
                    dft_arr = __DFSHelper(dft_arr, neighbor[0])

            return dft_arr
        
        start_node = self.getNode(start_node)
        dfs = __DFSHelper([], start_node)
        self.resetNodes() # Resets the nodes for graph to be searched again
        if len(dfs) == len(self.nodes): # If all nodes have been visited:
            return dfs
        else:
            return None


    # Performs a depth-first search for the end node, and returns the path to it if found.
    def DFSRec(self, start_node=0, end_node=1):
        
        def __DFSHelper(dfs_arr, curr_node, found=False):
            curr_node.visited = True
            dfs_arr.append(curr_node)

            if curr_node.val == str(end_node): #  Checks if the string value of the node is equal to the stringified end_node. 
                found = True
            else:
                for neighbor in curr_node.connections:
                    if neighbor and not found and not neighbor[0].visited:
                        dfs_arr, found = __DFSHelper(dfs_arr, neighbor[0], found)

            return dfs_arr, found
        
        start_node = self.getNode(start_node)
        dfs, found = __DFSHelper([], start_node)
        self.resetNodes() # Resets the nodes for graph to be searched again
        if found:
            return dfs
        else:
            return None


    # 3(e)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> DFTIter(final Node start, final Node end), which iteratively returns an ArrayList of the Nodes in the Graph in a valid Depth-First Search order. The first node in the array should be start and the last should be end. If no valid DFS path goes from start to end, return null.
    def DFTIter(self, start_node):
        stack, visited = [], []
        curr_node = self.getNode(start_node) # Ensures that start_node is a Node object.
        
        curr_node.visited = True # Mark current node visited.
        stack.append(curr_node) # Stacks the node.

        while len(stack) > 0: # While there are nodes in the stack
            curr_node = stack.pop() # Pops the top node and makes it the current one.
            visited.append(curr_node) # Add it to the visited list.
            curr_node.visited = True # Marks the node visited

            for neighbor in curr_node.connections: # Loops through the neighbors:
                if not neighbor[0].visited:
                    stack.append(neighbor[0]) # Stacks the unvisited neighbors.

        self.resetNodes() # Resets the nodes for graph to be searched again
        if len(visited) == len(self.nodes): # If all nodes have been visited:
            return visited
        else:
            return None


    # Performs a depth-first search for end_node iterativly, and returns the path if found:
    def DFSIter(self, start_node, end_node):
        stack, visited = [], []
        curr_node = self.getNode(start_node) # Ensures that start_node is a Node object.
        
        curr_node.visited = True # Mark current node visited.
        stack.append(curr_node) # Stacks the node.

        while len(stack) > 0: # While there are nodes in the stack
            curr_node = stack.pop() # Pops the top node and makes it the current one.
            visited.append(curr_node) # Add it to the visited list.
            curr_node.visited = True # Marks the node visited

            if curr_node.val == str(end_node):
                self.resetNodes() # Resets the nodes for graph to be searched again:
                return visited
            else:
                for neighbor in curr_node.connections: # Loops through the neighbors:
                    if not neighbor[0].visited:
                        stack.append(neighbor[0]) # Stacks the unvisited neighbors.

        self.resetNodes() # Resets the nodes for graph to be searched again
        return None # If node was not found, returns None


    # 3(f)	(3 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTRec(final Graph graph), which recursively returns an ArrayList of the Nodes in the Graph in a valid Breadth-First Traversal order.
    def BFTRec(self, start_node=0):

        def __BFTHelper(visited, curr_node, found=False):
            curr_node.visited = True
            visited.append(curr_node)
           
            for neighbor in curr_node.connections:
                if neighbor and not found and not neighbor[0].visited:
                    visited = __BFTHelper(visited, neighbor[0], found)

            return visited
        
        start_node = self.getNode(start_node)
        bft = __BFTHelper([], start_node)
        self.resetNodes() # Resets the nodes for graph to be searched again
        if len(bft) == len(self.nodes): # If all nodes have been visited:
            return bft
        else:
            return None


    # Performs a breadth-first-search for a node Recursivly, and returns the path to it if found:
    def BFSRec(self, start_node=0, end_node=1):

        def __BFTHelper(visited, curr_node, found=False):
            curr_node.visited = True
            visited.append(curr_node)
           
            if curr_node.val == end_node:
                return visited, True
            else:
                for neighbor in curr_node.connections:
                    if neighbor and not found and not neighbor[0].visited:
                        visited, found = __BFTHelper(visited, neighbor[0], found)

            return visited, found
        
        start_node, end_node = self.getNode(start_node), str(end_node)
        bft, found = __BFTHelper([], start_node)
        self.resetNodes() # Resets the nodes for graph to be searched again
        if found:
            return bft
        else:
            return None


    # 3(g)	(5 points) (You must submit code for this question!) In your GraphSearch class, implement ArrayList<Node> BFTIter(final Graph graph), which iteratively returns an ArrayList of all of the Nodes in the Graph in a valid Breadth-First Traversal.
    def BFTIter(self, start_node):
        queue, visited = [], []
        curr_node = self.getNode(start_node)
        curr_node.visited = True # Mark visited
        queue.append(curr_node)

        # While there are nodes in the queue:
        while len(queue) > 0: 
            curr_node = queue.pop(0) # Gets the first node in the queue
            curr_node.visited = True # Marks the node as visited
            visited.append(curr_node) # Adds it to the visited list

            for connection in curr_node.connections:
                neighbor = connection[0]
                if not neighbor.visited:
                    queue.append(neighbor)
        
        self.resetNodes() # Resets the nodes for graph to be searched again
        if len(visited) == len(self.nodes): # If all nodes have been visited:
            return visited
        else:
            return None


    # Performs a breadth-first search for end_node iteratively, and returns the path if found:
    def BFSIter(self, start_node, end_node):
        queue, visited = [], []
        curr_node = self.getNode(start_node)
        end_node = str(end_node)
        
        curr_node.visited = True # Mark visited
        queue.append(curr_node)

        # While there are nodes in the queue:
        while len(queue) > 0: 
            curr_node = queue.pop(0) # Gets the first node in the queue
            curr_node.visited = True # Marks the node as visited
            visited.append(curr_node) # Adds it to the visited list

            if curr_node.val == end_node:
                self.resetNodes() # Resets the nodes for graph to be searched again
                return visited
            else:
                for connection in curr_node.connections:
                    neighbor = connection[0]
                    if not neighbor.visited:
                        queue.append(neighbor)
        
        self.resetNodes() # Resets the nodes for graph to be searched again
        return None # If node was not found, returns None


    def printYellow(txt): print("\033[93m {}\033[00m" .format(txt)) 


    def printResult(self, result):
        if result:
            for i in range (len(result)-1):
                print(result[i].val, end='->')

            GraphSearch.printYellow(result[len(result)-1].val)
        else:
            print("\nNo path found")


if __name__ == "__main__":
    print("Creating Graph...")
    graph = GraphSearch()
    for i in range(10):
        graph.addNode(i)

    for i in range(1, 9):
        graph.addUndirectedEdge(i, i+1)

    print(graph)()

    print("Adding Edge...")
    graph.addUndirectedEdge("0", "1")
    graph.addUndirectedEdge("1", "2")

    print("Doing Searches...")
    graph.printResult(graph.DFSRec(0, 2))
    graph.printResult(graph.DFSIter(0, 2))
    graph.printResult(graph.BFSRec(0, 2)) 
    graph.printResult(graph.BFSIter(0, 2))

    print("Doing Traversals...")
    graph.printResult(graph.DFTRec(0))
    graph.printResult(graph.DFTIter(0))
    graph.printResult(graph.BFTRec(0)) 
    graph.printResult(graph.BFTIter(0))