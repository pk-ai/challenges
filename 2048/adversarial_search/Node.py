class Node:
    def __init__(self, state, depth, step, parent, score=0):
        self.state = state
        self.depth = depth
        self.step = step
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score