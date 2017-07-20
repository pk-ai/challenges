class Node:
    def __init__(self, grid, depth, step, parent, score=0):
        self.grid = grid
        self.depth = depth
        self.step = step
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score