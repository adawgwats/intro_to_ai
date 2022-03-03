from vertex import Vertex
class Node(Vertex):
    def __init__(self, name, value, weight, neighbors=None):
        """Initialize a Node object

        Args:
            name string: unique node ID.
            value float: value of node
            weight float: weight of node
            next (list of nodes, optional): Neighbors of this node. Defaults to None.
        """
        self.neighbors = neighbors
        super(Node, self).__init__(name, value, weight)


    def get_neighbors(self, target_value, max_weight, list_of_nodes, current_weight):
        """Function to find the acceptable neighbors of a node

        Args:
            target_value float: goal value on the knapsack
            max_weight float: max weight of an arrangement of objects
            list_of_nodes list of nodes: array of nodes
            current_weight float: current weight of an arrangement of objects
        """
        neighbors = []
        for node in list_of_nodes:
            if self.name >= node.name:
                continue
            potential_weight = node.weight + current_weight
            if potential_weight > max_weight:
                continue
            neighbors.append(node)
        return neighbors

            