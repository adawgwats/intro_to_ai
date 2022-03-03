from node import Node
from hillclimbing import HillClimbing
from vertex import Vertex
import argparse
from random import randint
from iterativedeepening import IterativeDeepening

MAXVAL = 99999999
def create_args():
    """Method for creating arguments
    """
    parser = argparse.ArgumentParser(description="Proccess arguments for knapsack problem")
    parser.add_argument("--file_path", help="Path to input file(.txt)")
    parser.add_argument("--mode", help="specify whether the algorithm uses iterative deepening (ID) or Hill climbing (HC) mode")
    return parser.parse_args()

def read_input_file(file_path):
    """path to input file
    Args:
        file_path string: path to file containing input
    """
    try:
        with open(file_path) as f:
            lines = f.readlines()
            #remove any \n or ' ' at the end of each element in the array
            for index,value in enumerate(lines):
                lines[index] = value.rstrip("\n ")
        f.close()
        return lines
    except Exception as e:
        print(e)
        exit(0)
        
        
def create_vertex_list(vertex_list, isNode=False):
    """Creates objects of type vertex from the input file
    Args:
        vertex_list list: a list of strings, where each string has 3 components separated by spaces
        isNode (bool, optional): Used to call the node class which is used in ID algo. Defaults to False.
    Returns:
        list:list of objects of type vertex or node
    """
    list_of_vertices = []
    for current_vertex in vertex_list:
        component = current_vertex.split()
        if isNode:
            list_of_vertices.append(Node(component[0], float(component[1]), float(component[2])))
        else:
            list_of_vertices.append(Vertex(component[0], float(component[1]), float(component[2])))
    return list_of_vertices

    
def create_starting_state(vertex_list):
    """Used to initalize the starting state for HC algo
    Args:
        vertex_list list: list of objects of type vertex
    Returns:
        list: list of objects of type vertex
    """
    start_state = []
    for vertex in vertex_list:
        rand_num = randint(0,1)
        if rand_num == 0:
            start_state.append(vertex.name)   
    return start_state


def print_state(set_state):
    if not set_state:
        print("Nothing to print")
        return
    for vertex in set_state:
        print(vertex.name, sep ='', end=' ')
    print()
    
    
if __name__ == "__main__":
    args = create_args()
    lines = read_input_file(args.file_path)
    target_value = float(lines[0].split()[0])
    max_weight = float(lines[0].split()[1])
    
    if args.mode == "ID":
        vertex_list = create_vertex_list(lines[1:], isNode = True)
        ID = IterativeDeepening(vertex_list, target_value,max_weight)
        ID.ids()
    elif args.mode == "HC":
        vertex_list = create_vertex_list(lines[1:])
        list_of_optimal_states = []
        for restart in range(10):
            print("Restart Num:", str(restart))
            start_state = create_starting_state(vertex_list)
            HC = HillClimbing(start_state, vertex_list, target_value, max_weight)
            optimal_state = HC.climb_hill()
            list_of_optimal_states.append(optimal_state)
            print("-------------------------------------------------------------------------")
        best_choice = HC.neighbor_evaluation(list_of_optimal_states)
        print("Optimal State: ")
        for chr in best_choice[0]:
            print(chr, end=" ")
        print()
    else:
        print("Invalid input for --mode. Please provide either 'ID' for iterative deepening or 'HC' for Hill Climbing")
        exit(0)
    
