#!/usr/bin/python3
# python <file>.py <initial_state> <final_state>
# python 8-puzzle/bfs.py 1,2,5,3,4,0,6,7,8 0,1,2,3,4,5,6,7,8
# For Debugging in Visual Code, Run these commands in Debug Console. sys.argv.append("3,1,2,0,4,5,6,7,8") sys.argv.append("0,1,2,3,4,5,6,7,8")
import sys
class Node:
    def __init__(self, state, depth, step, parent):
        self.state = state
        self.depth = depth
        self.step = step
        self.parent = parent

def getPathtoGoal(node, path_to_goal):
    if node.step == None:
        return path_to_goal
    else:
        path_to_goal.insert(0, node.step)
        return getPathtoGoal(node.parent, path_to_goal)

def getSteps(node_state):
    empty_space_index = node_state.index(0)
    if empty_space_index == 0:
        return [('Down', 3), ('Right', 1)]
    elif empty_space_index == 1:
        return [('Down', 4), ('Left', 0), ('Right', 2)]
    elif empty_space_index == 2:
        return [('Down', 5), ('Left', 1)]
    elif empty_space_index == 3:
        return [('Up', 0), ('Down', 6), ('Right', 4)]
    elif empty_space_index == 4:
        return [('Up', 1), ('Down', 7), ('Left', 3), ('Right', 5)]
    elif empty_space_index == 5:
        return [('Up', 2), ('Down', 8), ('Left', 4)]
    elif empty_space_index == 6:
        return [('Up', 3), ('Right', 7)]
    elif empty_space_index == 7:
        return [('Up', 4), ('Left', 6), ('Right', 8)]
    else:
        return [('Up', 5), ('Left', 7)]

def bfs(initial_state, given_goal_state):
    init_state = list(map(int, initial_state.split(',')))
    goal_state = list(map(int, given_goal_state.split(',')))
    total_nodes_visited = 0
    nodes_list = []
    visited_states = []
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing BFS to solve.")
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
                    path_to_goal = getPathtoGoal(node, path_to_goal)
                    return path_to_goal
                else:
                    steps = getSteps(node.state)
                    for step in steps:
                        new_state = node.state[:]
                        old, new = node.state.index(0), step[1]
                        new_state[new], new_state[old] = new_state[old], new_state[new]
                        if new_state not in visited_states:
                            nodes_list.append(Node(new_state, node.depth + 1, step[0], node))

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        path_to_goal = bfs(sys.argv[1], sys.argv[2])
        print(path_to_goal)