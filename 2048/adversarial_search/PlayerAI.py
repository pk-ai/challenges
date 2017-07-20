
from random import randint
from BaseAI import BaseAI
import time
timeTimlimit  = 0.2
prevTime =  0
currentTime = 0
class PlayerAI(BaseAI):
    def getMove(self, grid):
        prevTime =  time.clock()
        currentTime = time.clock()
        #while currentTime - prevTime < timeTimlimit:
            #print("IN WHILE")
        #    currentTime = time.clock()
        moves = grid.getAvailableMoves()
        print(heuristic_eval_board(grid))
        if moves:
            if len(moves) > 1:
                return moves[randint(0, len(moves) - 1)]
            else:
                return moves[0]
        else:
            return None

def maximize(grid, alpha, beta):
    pass

def minimize(grid, alpha, beta):
    pass

def heuristic_eval_board(grid):
    # Inspired from the response https://stackoverflow.com/a/22498940
    # 1. Granting "bonuses" 
    #   a. for open squares
    #   b. for having large values on the edge.
    total_score = 0
    empty_cells_score = len(grid.getAvailableCells())
    # What is the weight of empty cells heuristic
    total_score += empty_cells_score
    max_tiles = getMaxTiles(grid)
    max_tiles_socre = 0
    board_edges = [(0,0),(0, grid.size -1), (grid.size-1, 0), (grid.size-1, grid.size-1)]
    for el in board_edges:
        if grid.map[el[0]][el[1]] in max_tiles:
            # Shall we add max_tile score value or just add 1 as bonus
            max_tiles_socre += 1
    # What is the weight for large values on edge
    total_score += max_tiles_socre
    return total_score

# Return the Tiles with Maximum Value (at max of 4, since any square grid contains only 4 edges)
def getMaxTiles(givenGrid):
    grid = givenGrid.clone()
    maxTiles = []
    while len(maxTiles) != 4 and notEmptyGrid(grid):
        maxTile = 0
        el_x, el_y = 0, 0
        for x in range(grid.size):
            for y in range(grid.size):
                if grid.map[x][y] != 0 and maxTile < grid.map[x][y]:
                    maxTile = grid.map[x][y]
                    el_x, el_y = x, y
        if maxTile not in maxTiles:
            maxTiles.append(maxTile)
        grid.map[el_x][el_y] = 0
    return maxTiles

def notEmptyGrid(grid):
    for x in range(grid.size):
        for y in range(grid.size):
            if grid.map[x][y] != 0:
                return True
    return False
