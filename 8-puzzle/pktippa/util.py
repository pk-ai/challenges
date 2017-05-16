class Node:
    def __init__(self, state, depth, step, parent, score=0):
        self.state = state
        self.depth = depth
        self.step = step
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

def getPathtoGoal(node):
    path_to_goal = []
    while node.step:
        path_to_goal.insert(0, node.step)
        node = node.parent
    return path_to_goal

def getSteps(node_state):
    empty_space_index = node_state.index("0")
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