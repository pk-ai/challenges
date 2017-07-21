from random import randint
from BaseAI import BaseAI
from Node import Node
import time, math
from heapq import heappush, heappop
timeTimlimit  = 0.2
prevTime =  0
currentTime = 0
node_depth = 4
possibleNewTiles = [2, 4]
defaultProbability = 0.9
class PlayerAI(BaseAI):
    def getMove(self, grid):
        prevTime =  time.clock()
        currentTime = time.clock()
        #while currentTime - prevTime < timeTimlimit:
            #print("IN WHILE")
        #    currentTime = time.clock()
        moves = grid.getAvailableMoves()
        if moves:
            if len(moves) > 1:
                first_node = Node(grid,0,-1,None,0)
                (node, score) = maximize(first_node, -math.inf, math.inf)
                if node:
                    return node.move
                else:
                    return moves[randint(0, len(moves) - 1)]
            else:
                return moves[0]
        else:
            return None

def maximize(given_node, alpha, beta):
    if given_node.depth == node_depth:
        return (None, given_node.score)
    (maxChild, maxUtility) = (None, -math.inf)
    max_child_nodes = get_max_child_nodes(given_node)
    while max_child_nodes:
        child = heappop(max_child_nodes)[1]
        (_, utility) = minimize(child, alpha, beta)
        if utility > maxUtility:
            (maxChild, maxUtility) = (child, utility)
        if maxUtility >= beta:
            break;
        if maxUtility > alpha:
            alpha = maxUtility
    return (maxChild, maxUtility)

def minimize(given_node, alpha, beta):
    if given_node.depth == node_depth:
        return (None, given_node.score)
    (minChild, minUtility) = (None, math.inf)
    min_child_nodes = get_min_child_nodes(given_node)
    while min_child_nodes:
        child = heappop(min_child_nodes)[1]
        (_, utility) = maximize(child, alpha, beta)
        if utility < minUtility:
            (minChild, minUtility) = (child, utility)
        if minUtility <= alpha:
            break;
        if minUtility < beta:
            beta = minUtility
    return (minChild, minUtility)

def get_max_child_nodes(given_node):
    moves = given_node.grid.getAvailableMoves()
    max_child_nodes = []
    for mv in moves:
        cloned_grid = given_node.grid.clone()
        cloned_grid.move(mv)
        score = heuristic_eval_board(cloned_grid)
        child_node = Node(cloned_grid,given_node.depth+1,mv,given_node,score)
        heappush(max_child_nodes, (score, child_node))
    return max_child_nodes

def get_min_child_nodes(given_node):
    min_child_nodes = []
    available_cells = given_node.grid.getAvailableCells()
    for ac in available_cells:
        cloned_grid = given_node.grid.clone()
        if cloned_grid.canInsert(ac):
            cloned_grid.setCellValue(ac, getNewTileValue())
            score = heuristic_eval_board(cloned_grid)
            child_node = Node(cloned_grid,given_node.depth+1,-1,given_node,score)
            # Do we have to push with -score or score - Which one can lead to max pruning ?
            heappush(min_child_nodes, (-score, child_node))
    return min_child_nodes

def getNewTileValue():
    if randint(0,99) < 100 * defaultProbability:
        return possibleNewTiles[0]
    else:
        return possibleNewTiles[1]
    
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
            max_tiles_socre += grid.map[el[0]][el[1]]
    # What is the weight for large values on edge
    total_score += max_tiles_socre
    # More heuristics to add as follows
    # a.) Number of potential merges
    # b.) Keep the big tiles on edges and keep the next big tiles like a snake
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
