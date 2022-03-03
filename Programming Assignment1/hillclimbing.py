from knapsack import KnapSack
class HillClimbing():
    def __init__(self, starting_state, vertex_list, target_value, max_weight ):
        self.knapsack = KnapSack(vertex_list, target_value, max_weight)
        self.vertex_list = self.knapsack.vertex_list
        self.target_value = target_value
        self.max_weight = max_weight
        self.starting_state = starting_state
        self.MAXINT = 999999999
    
    def climb_hill(self):
        """Main method that runs the hill climbing algorithm

        Returns:
            list of vertices: List of nodes which was the optimal choice given the parameters
        """
        current_value = self.cost_function(self.starting_state)
        current_state = self.starting_state
        iteration = 0
        self.print_state_and_value(current_state, iteration)
        while(True):
            list_of_neighbors = self.find_neighbors(current_state)
            optimal_neighbor, optimal_value = self.neighbor_evaluation(list_of_neighbors)
            if optimal_value >= current_value:
                return current_state
            current_state = optimal_neighbor
            current_value = optimal_value
            iteration+=1
            self.print_state_and_value(current_state, iteration)
            
            
    def cost_function(self, vertex_value_list):
        """This is the cost function as outlined in the homework
        Args:
            vertex_value_list list: list of characters which correspond to vertex IDs
        Returns:
            float: the evaulation of the function given the arguments in the set
        """
        value = 0
        weight = 0
        if vertex_value_list:
            #If the list is the empty list, then the value is 0 and weight is 0
            for element in vertex_value_list:
                vertex = self.get_vertex(element, self.vertex_list)
                value += vertex.value
                weight += vertex.weight
        weight_penalty = max(weight - self.max_weight,0)
        value_penalty = max(self.target_value - value,0)
        return weight_penalty + value_penalty
    
    def get_vertex(self, name, vertex_list):
        """Useful to lookup vertices stored in dictionary by their name
        Args:
            name string: vertex ID
            vertex_list string: complete set of vertices
        Returns:
            vertex: returns vertex object or None
        """
        for vertex in vertex_list:
            if vertex.name == name:
                return vertex
        return None
    
    def find_neighbors(self, current_set):
        """Given a set of vertices, find the neighbors of the set. A neighbor is defined to be any set which is exactly one operation away
        Args:
            current_set list: list of vertex names
        Returns:
            list: list of neighbors
        """
        list_of_neighbors = []
        # remove duplicate vertices in the complete set and the current set
        verticies = [vertex.name for vertex in self.vertex_list]
        verticies_to_remove = []
        for vertex in verticies:
            for element in current_set:
                if vertex == element:
                    verticies_to_remove.append(vertex)
                    break
        for vertex in verticies_to_remove:
            verticies.remove(vertex)
        list_of_neighbors = self.add_operation(current_set, verticies, list_of_neighbors)
        list_of_neighbors = self.remove_operation(current_set, list_of_neighbors)
        list_of_neighbors = self.swap_operation(current_set, verticies, list_of_neighbors)
        return list_of_neighbors
    
    def neighbor_evaluation(self, list_of_neighbors):
        """Useful for evaulating lists of nodes through our cost function

        Args:
            list_of_neighbors list: list of sets of vertices (strings)

        Returns:
            tuple: returns a tuple where the first index is the set and the second is its error value
        """
        optimal_neighbor = []
        optimal_value = self.MAXINT
        for neighbor in list_of_neighbors:
            error_value = self.cost_function(neighbor)
            if  error_value < optimal_value:
                optimal_neighbor = neighbor
                optimal_value = error_value
        return optimal_neighbor, optimal_value
    
    def add_operation(self, current_set, vertex_value_list, list_of_neighbors):
        """function to check for valid appendices to the current set

        Args:
            current_set list: list of vertices (strings)
            vertex_value_list list: list of all vertices by name
            list_of_neighbors list: list of vertex names currently unused
        Returns:
            list: list of list of strings
        """
        if not vertex_value_list:
            return list_of_neighbors
        for vertex in vertex_value_list:
            dup_current_set = self.copy_vertex_list(current_set)
            dup_current_set.append(vertex)
            list_of_neighbors.append(dup_current_set)
        return list_of_neighbors
            
    def remove_operation(self, current_set, list_of_neighbors):
        #Edge case: empty set is passed
        if not current_set:
            return list_of_neighbors
        for vertex in current_set:
            new_vertex = self.copy_vertex_list(current_set)
            new_vertex.remove(vertex)
            list_of_neighbors.append(new_vertex)
        return list_of_neighbors

    def swap_operation(self, current_set, vertex_value_list, list_of_neighbors):
        """Adds to the list of neighbors all the sets that can be created by swaping one vertex in the current set from one not in it

        Args:
            current_set list: list of vertex values (Characters) in the current state
            vertex_list lsit: list of all vertices in the problem where duplicates from the current set are removed
            list_of_neighbors list of lists: list of neighbors

        Returns:
            list of lists: list of neighbors
        """
        #Edge case: empty set is passed
        if not current_set:
            return list_of_neighbors
        for index,value in enumerate(vertex_value_list):
            for jndex, vertex in enumerate(current_set):
                neighbor =  self.copy_vertex_list(current_set)
                neighbor[jndex] = value
                list_of_neighbors.append(neighbor)
        return list_of_neighbors
    
    def copy_vertex_list(self, vertex_value_list):
        copied_verticies = []
        for vertex in vertex_value_list:
            copied_verticies.append(vertex)
        return copied_verticies
    
    
    def print_state_and_value(self, current_state, iteration):
        cost_value = self.cost_function(current_state)
        vertex_names = [vertex for vertex in current_state]
        print("Iteration:", iteration, "Current State:", vertex_names, "Function value:", cost_value)