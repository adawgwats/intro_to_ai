class KnapSack():
    def __init__(self, vertex_list, target_value=20, max_weight=10):
        """Initialization method for knapsack class.

        Args:
            vertex_list list: list of vertices
            target_value (int, optional):   Target Value attempted to achieve. Defaults to 20.
            max_weight (int, optional): [description]. Defaults to 10.
        """
        self.vertex_list = vertex_list
        self.target_value = target_value
        self.max_weight = max_weight
        self.best_option = []
        
    def add_vertex(self, vertex):
        """Add a vertex to the list of vertices

        Args:
            vertex Object: A vertex object
        """
        self.vertex_list.append(vertex)
    
    def remove_vertex(self, vertex):
        """Removes a vertex from the list of vertices

        Args:
            vertex Object: vertex to be removed
        """
        self.vertex_list.remove(vertex)
        
    def set_best_set(self, vertex_list):
        """Sets the current ideal vertex set

        Args:
            vertex_list list: list of vertices
        """
        self.best_option = vertex_list