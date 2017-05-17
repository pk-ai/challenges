#!/usr/bin/python3
# python <file>.py <initial_state> <final_state>
# python 8-puzzle/a_star.py 8,6,4,2,1,3,5,7,0 0,1,2,3,4,5,6,7,8
# For Debugging in Visual Code, Run these commands in Debug Console. sys.argv.append("3,1,2,0,4,5,6,7,8") sys.argv.append("0,1,2,3,4,5,6,7,8")
# Tests 6,1,8,4,0,2,7,3,5 -> ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up']
# 8,6,4,2,1,3,5,7,0 -> ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left']
import sys, time
from heapq import heappush, heappop
from pktippa.util import Node, getPathtoGoal, getSteps
goal_state = []
goal_state_matrix = []

# Score considering number of displaced tiles other than 0 or empty space
#def getScore(initial_state, goal_state):
#    return sum([1 if initial_state[i] != "0" and initial_state[i] != goal_state[i] else 0 for i in range(0,9)])

# Score considering manhattan distance.
def getScore(initial_state):
    sum = 0
    nums = ["1","2","3","4","5","6","7","8"]
    inital_state_matrix = list(getMatrix(initial_state))
    for num in nums:
        (i,j) = getMatrixPos(inital_state_matrix, num)
        (k,l) = getMatrixPos(goal_state_matrix, num)
        # Manhattan distance for grid/matrix
        sum += abs(i-k) + abs(j-l)
    return sum

# Converting [8,6,4,2,1,3,5,7,0] to matrix [[8, 6, 4], [2, 1, 3], [5, 7, 0]]
def getMatrix(state):
    for i in range(0, len(state), 3):
        yield state[i:i + 3]

# Getting the (row, column) of respective element in matrix.
def getMatrixPos(states_matrix, num):
    for i in range(0,3):
        for j in range(0,3):
            if states_matrix[i][j] == num:
                return (i,j)

# Performs a star algorithm to solve 8-puzzle game.
def a_star(initial_state, given_goal_state):
    init_state = initial_state.split(',')
    global goal_state
    goal_state = given_goal_state.split(',')
    total_nodes_visited = 0
    nodes_list = []
    states_list = set()
    visited_states_count = 0
    max_search_depth = 0
    global goal_state_matrix
    goal_state_matrix = list(getMatrix(goal_state))
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing A Star to solve.")
        first_node = Node(init_state, 0, None, None, 0)
        heappush(nodes_list, (0, first_node))
        states_list.add("".join(init_state))
        path_to_goal = []

        while True:
            if not nodes_list:
                return path_to_goal, visited_states_count, max_search_depth, 0
            else:
                # Need to use a Priority Queue, pop will give the element with the priority set
                heap_node = heappop(nodes_list)
                node = heap_node[1]
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
                            score = getScore(new_state) + node.depth + 1
                            new_node = Node(new_state, node.depth + 1, step[0], node, score)
                            heappush(nodes_list, (score, new_node))
                            max_search_depth = (node.depth + 1) if (node.depth + 1) > max_search_depth else max_search_depth
                            states_list.add(new_state_str)
                visited_states_count += 1

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        start = time.time()
        path_to_goal, nodes_expanded, max_search_depth, node_depth = a_star(sys.argv[1], sys.argv[2])
        print("Path to goal: ", path_to_goal)
        print("total Nodes Expanded or visited nodes: ", nodes_expanded)
        print("Max Search Depth: ", max_search_depth)
        print("Find Node Depth: ", node_depth)
        print("Total time took - ", time.time() - start)