# python3 projects/graph/graph.py
# python3 projects/graph/test_graph.py -v

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        to_visit = Queue()            # Create a queue to hold nodes to visit
        visited = set()               # Create a set to hold visited nodes
        
        # Initalize: add the starting node to the queue
        to_visit.enqueue(starting_vertex) 
        # While queue not empty:
        while to_visit.size() > 0:
            v = to_visit.dequeue()    # dequeue first entry

            # if not visited:
            if v not in visited:
                print(v)              # Visit the node (print it out)
                visited.add(v)        # Add it to the visited set

                # enqueue all its neighbors
                for i in self.get_neighbors(v):
                    to_visit.enqueue(i)   # print(f"Adding: {n}")

    def dft(self, starting_vertex):
        """
        Print each vertex .in depth-first order
        beginning from starting_vertex.
        """
        to_visit = Stack()              # Create a stack to hold nodes to visit
        visited = set()                 # Create a set to hold visited nodes

        # Initalize: add the starting node to the stack
        to_visit.push(starting_vertex)
        # While stack not empty:
        while to_visit.size() > 0:
            v = to_visit.pop()          # remove the last entry

            # if not visited:
            if v not in visited:
                print(v)                # Visit the node (print it out)
                visited.add(v)          # Add it to the visited set

                # add to stack all its neighbors
                for i in self.get_neighbors(v):
                    to_visit.push(i)    # print(f"Adding: {n}")

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        to_visit = Queue()     # Create an empty queue 
        visited = set()        # Create a Set to store visited vertices
        path = []
        path.append(starting_vertex)
        to_visit.enqueue(path)  # Enqueue A PATH TO the starting vertex ID

        # While the queue is not empty...
        while to_visit.size() > 0:
            p = to_visit.dequeue()       # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
            if p[-1] not in visited:
                if p[-1] == destination_vertex:   # CHECK IF IT'S THE TARGET
                    return p                      # IF SO, RETURN PATH
                else:
                    visited.add(p[-1])
                    for neighbor in self.get_neighbors(p[-1]):
                        new_path = p.copy()
                        new_path.append(neighbor)
                        to_visit.enqueue(new_path) 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        to_visit = Stack()              # Create a stack to hold nodes to visit
        visited = set()                 # Create a set to hold visited nodes
        path = []
        path.append(starting_vertex)
        to_visit.push(path)             # Initalize: add A PATH TO the starting vertex 

        # While stack not empty:
        while to_visit.size() > 0:
            p = to_visit.pop()       # Pop the last PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
            if p[-1] not in visited:
                if p[-1] == destination_vertex:   # CHECK IF IT'S THE TARGET
                    return p                      # IF SO, RETURN PATH
                else:
                    visited.add(p[-1])
                    for neighbor in self.get_neighbors(p[-1]):
                        new_path = p.copy()
                        new_path.append(neighbor)
                        to_visit.push(new_path) 

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, path, visited)
                if new_path:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
