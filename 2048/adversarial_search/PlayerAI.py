
from random import randint
from BaseAI import BaseAI
import time
timeTimlimit  = 0.2
class PlayerAI(BaseAI):
    def getMove(self, grid):
        prevTime =  time.clock()
        currentTime = time.clock()
        while currentTime - prevTime < timeTimlimit:
            print("IN WHILE")
            currentTime = time.clock()
        moves = grid.getAvailableMoves()
        return moves[randint(0, len(moves) - 1)] if moves else None