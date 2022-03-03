from knapsack import KnapSack
from node import Node

class IterativeDeepening():
    def __init__(self, node_list, target_value, max_weight, cost_function=None):
        self.KnapSack = KnapSack(node_list, target_value=target_value, max_weight=max_weight)
        self.node_list = self.KnapSack.vertex_list
        self.create_node_dict()
        self.target_value = target_value
        self.max_weight = max_weight
        self.val = ""
        
    def create_node_dict(self):
        self.node_dict = {}
        for node in self.node_list:
            self.node_dict[node.name] = node
        
    
    def ids(self):
        """This is the main iterative deepening algorithm. It's worth noting that this algorithm will find all
            solutions which lie on the same level as the first soltion found.
        """
        for level in range(len(self.node_list)):
            self.DFS(None, 0, level, 0, [])
            if self.val:
                print("Solution(s) found when set consists of: ", self.val)
                exit(0)
        print("No Solution")
    
    def DFS(self, root, current_level, max_depth, current_weight, nodes_currently_in_list):
        """Main DFS algorithm

        Args:
            root node: node which to begin dfs from
            current_level int: current level in tree
            max_depth int: max depth to traverse in the tree
            current_weight float: current weight of the set
            nodes_currently_in_list list: current construction of the set

        Returns:
            bool: returns false if max depth is reached or leaf with no solution is reached
        """
        if current_level > max_depth:
            return False
        if self.is_target_value(nodes_currently_in_list):
            if self.val:
                self.val += " or "
            for node in nodes_currently_in_list:
                self.val += node.name + " "
            return True
        neighbors = []
        if root:
            neighbors = root.get_neighbors(self.target_value, self.max_weight, self.node_list, current_weight)
        else:
            neighbors = self.get_starting_neighbors()
        if not neighbors:
            return False
        neighbors.sort(key=lambda x: x.name)
        for node in neighbors:
            nodes_currently_in_list.append(node)
            self.DFS(node, current_level+1, max_depth, current_weight + node.weight, nodes_currently_in_list)  
            nodes_currently_in_list.remove(node)
            
            
    def is_target_value(self, node_list):
        """To save computational time, this flag is put in place to prevent from travesing further down a level than needed
        Args:
            node_list list: list of characters
        """
        if not node_list:
            if self.target_value > 0:
                return False
            else:
                return True
        value = 0
        weight = 0
        for node in node_list:
            value += node.value
            weight += node.weight
        if weight > self.max_weight:
            return False
        if value >= self.target_value:
            return True                                                     
    
    
    def get_starting_neighbors(self):
        """This method handles the case where DFS is starting from the empty list
        """
        start_list = []
        for neighbor in self.node_list:
            if neighbor.weight < self.max_weight:
                start_list.append(neighbor)
        return start_list


    def print_node_list(self, node_list):
        for node in node_list:
            print(node.name, end="")
        print()