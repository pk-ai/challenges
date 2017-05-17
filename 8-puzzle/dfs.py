#!/usr/bin/python3
# python <file>.py <initial_state> <final_state>
# python 8-puzzle/dfs.py 1,2,5,3,4,0,6,7,8 0,1,2,3,4,5,6,7,8
# For Debugging in Visual Code, Run these commands in Debug Console. sys.argv.append("3,1,2,0,4,5,6,7,8") sys.argv.append("0,1,2,3,4,5,6,7,8")
import sys, time
from pktippa.util import Node, getPathtoGoal, getSteps

def dfs(initial_state, given_goal_state):
    init_state = initial_state.split(',')
    goal_state = given_goal_state.split(',')
    total_nodes_visited = 0
    nodes_list = []
    states_list = set()
    max_search_depth = 0
    visited_states_count = 0
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing DFS to solve.")
        first_node = Node(init_state, 0, None, None)
        nodes_list.append(first_node)
        states_list.add("".join(init_state))
        path_to_goal = []
        while True:
            if not nodes_list:
                return path_to_goal, visited_states_count, max_search_depth, 0
            else:
                node = nodes_list.pop(0)
                max_search_depth = node.depth if node.depth > max_search_depth else max_search_depth
                if node.state == goal_state:
                    path_to_goal = getPathtoGoal(node)
                    print("Remaining nodes list ", len(nodes_list))
                    return path_to_goal, visited_states_count, max_search_depth, node.depth
                else:
                    steps = getSteps(node.state)
                    # The below step is different from the BFS approach
                    # steps are reversed so that when adding steps to nodes_list stack,
                    # it has to be in sequence.
                    steps.reverse()
                    for step in steps:
                        new_state = node.state[:]
                        old, new = node.state.index("0"), step[1]
                        new_state[new], new_state[old] = new_state[old], new_state[new]
                        new_state_str = "".join(new_state)
                        if new_state_str not in states_list:
                            # The below step is different from the BFS approach
                            # DFS follows a stack "Last in First out", so element at the start
                            nodes_list.insert(0, Node(new_state, node.depth + 1, step[0], node))
                            max_search_depth = (node.depth + 1) if (node.depth + 1) > max_search_depth else max_search_depth
                            states_list.add(new_state_str)
                visited_states_count += 1

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        start = time.time()
        path_to_goal, nodes_expanded, max_search_depth, node_depth = dfs(sys.argv[1], sys.argv[2])
        # Prints big list of Path, to print the path uncomment and see.
        #print("Path to goal : ", path_to_goal)
        print("total Nodes Expanded or visited nodes: ", nodes_expanded)
        print("Max Search Depth: ", max_search_depth)
        print("Find Node Depth: ", node_depth)
        print("Total time took - ", time.time() - start)