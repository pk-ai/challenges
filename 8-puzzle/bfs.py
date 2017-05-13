#!/usr/bin/python3
# python <file>.py <initial_state> <final_state>
# python 8-puzzle/bfs.py 8,6,4,2,1,3,5,7,0 0,1,2,3,4,5,6,7,8
# For Debugging in Visual Code, Run these commands in Debug Console. sys.argv.append("3,1,2,0,4,5,6,7,8") sys.argv.append("0,1,2,3,4,5,6,7,8")
import sys, time
from pktippa.util import Node, getPathtoGoal, getSteps

def bfs(initial_state, given_goal_state):
    init_state = initial_state.split(',')
    goal_state = given_goal_state.split(',')
    total_nodes_visited = 0
    nodes_list = []
    states_list = set()
    visited_states_count = 0
    max_search_depth = 0
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing BFS to solve.")
        first_node = Node(init_state, 0, None, None)
        nodes_list.append(first_node)
        states_list.add("".join(init_state))
        path_to_goal = []
        while True:
            if not nodes_list:
                return path_to_goal, visited_states_count, max_search_depth, 0
            else:
                # Since BFS has to be implemented in Queue, which is First in First out
                # So we are retrieving the first element
                node = nodes_list.pop(0)
                max_search_depth = node.depth if node.depth > max_search_depth else max_search_depth
                if node.state == goal_state:
                    path_to_goal = getPathtoGoal(node)
                    print("Remaining nodes list ", len(nodes_list))
                    return path_to_goal, visited_states_count, max_search_depth, node.depth
                else:
                    steps = getSteps(node.state)
                    for step in steps:
                        new_state = node.state[:]
                        old, new = node.state.index("0"), step[1]
                        new_state[new], new_state[old] = new_state[old], new_state[new]
                        new_state_str = "".join(new_state)
                        if new_state_str not in states_list:
                            # Appending the element at the end, so pop(0) can work as Queue
                            nodes_list.append(Node(new_state, node.depth + 1, step[0], node))
                            max_search_depth = (node.depth + 1) if (node.depth + 1) > max_search_depth else max_search_depth
                            states_list.add(new_state_str)
                visited_states_count += 1

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        start = time.time()
        path_to_goal, nodes_expanded, max_search_depth, node_depth = bfs(sys.argv[1], sys.argv[2])
        print("Path to goal: ", path_to_goal)
        print("total Nodes Expanded or visited nodes: ", nodes_expanded)
        print("Max Search Depth: ", max_search_depth)
        print("Find Node Depth: ", node_depth)
        print("Total time took - ", time.time() - start)