#!/usr/bin/python3
# python <file>.py <initial_state> <final_state>
# python 8-puzzle/dfs.py 1,2,5,3,4,0,6,7,8 0,1,2,3,4,5,6,7,8
# For Debugging in Visual Code, Run these commands in Debug Console. sys.argv.append("3,1,2,0,4,5,6,7,8") sys.argv.append("0,1,2,3,4,5,6,7,8")
import sys, time
from pktippa.util import Node, getPathtoGoal, getSteps

def bfs(initial_state, given_goal_state):
    init_state = list(map(int, initial_state.split(',')))
    goal_state = list(map(int, given_goal_state.split(',')))
    total_nodes_visited = 0
    nodes_list = []
    states_list = []
    visited_states = []
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing DFS to solve.")
        first_node = Node(init_state, 0, None, None)
        nodes_list.append(first_node)
        path_to_goal = []
        while True:
            if not nodes_list:
                return None
            else:
                node = nodes_list.pop(0)
                visited_states.append(node.state)
                if node.state == goal_state:
                    path_to_goal = getPathtoGoal(node)
                    return path_to_goal
                else:
                    steps = getSteps(node.state)
                    # The below step is different from the BFS approach\
                    # steps are reversed so that when adding steps to nodes_list stack,
                    # it has to be in sequence.
                    steps.reverse()
                    for step in steps:
                        new_state = node.state[:]
                        old, new = node.state.index(0), step[1]
                        new_state[new], new_state[old] = new_state[old], new_state[new]
                        if new_state not in states_list and new_state not in visited_states:
                            # The below step is different from the BFS approach
                            # DFS follows a stack "Last in First out", so element at the start
                            nodes_list.insert(0, Node(new_state, node.depth + 1, step[0], node))
                            states_list.append(new_state)

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        start = time.time()
        path_to_goal = bfs(sys.argv[1], sys.argv[2])
        print(path_to_goal)
        print("Total time took - ", time.time() - start)