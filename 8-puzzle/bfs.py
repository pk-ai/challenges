#!/usr/bin/python3
# python 8-puzzle/bfs.py 0,1,2,3,4,5,6,7,8 1,2,5,3,4,0,6,7,8
import sys
class Node:
    def __init__(self, state, depth, step, parent):
        self.state = state
        self.depth = depth
        self.step = step
        self.parent = parent

def bfs(initial_state, given_goal_state):
    init_state = initial_state.split(',')
    goal_state = given_goal_state.split(',')
    total_nodes_visited = 0
    if len(init_state) != len(goal_state) or len(init_state) != 9 or len(goal_state) != 9:
        print("Invalid Input, please enter valid input.")
    else:
        print("Doing BFS to solve.")

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Please enter start state and goal state")
    else:
        bfs(sys.argv[1], sys.argv[2])