class Node:
    def __init__(self, grid, depth, move, parent, score=0):
        self.grid = grid
        self.depth = depth
        self.move = move
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score