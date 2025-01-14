"""
Only for logics
"""

playerCampsPos = [[[0, 5], [1, 5], [2, 5], [3, 5]], #Red
                  [[9, 0], [9, 1], [9, 2], [9, 3]], #Green
                  [[14, 9], [13, 9], [12, 9], [11, 9]], #Yellow
                  [[5, 14], [5, 13], [5, 12], [5, 11]]] #Blue

playerSpawns = [0, 14, 28, 42]

locationsPos = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6],
                [6, 6], 
                [6, 5], [6, 4], [6, 3], [6, 2], [6, 1], [6, 0], 
                [7, 0], 
                [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], 
                [8, 6], 
                [9, 6], [10, 6], [11, 6], [12, 6], [13, 6], [14, 6], 
                [14, 7], 
                [14, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], 
                [8, 8], 
                [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], 
                [7, 14], 
                [6, 14], [6, 13], [6, 12], [6, 11], [6, 10], [6, 9], 
                [6, 8], 
                [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], 
                [0, 7], 
                [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], #Red ladder
                [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], #Green ladder
                [13, 7], [12, 7], [11, 7], [10, 7], [9, 7], [8, 7], #Yellow ladder
                [7, 13], [7, 12], [7, 11], [7, 10], [7, 9], [7, 8]] #Blue ladder

def RunTurns(currentTurn, teams):
    """
    Used to set the new turn, return a int if a new turn is available or False if there's no turn left (everyone finished)
    """
    newTurn = currentTurn
    if newTurn >= 3:
        newTurn = 0
    else:
        newTurn += 1
    for h in range(5):
        if (teams[newTurn][h].Finished != False):
            return newTurn
        if(newTurn == currentTurn): return currentTurn
        else:
            if newTurn >= 3:
                newTurn = 0
            else:
                newTurn += 1
    return False
    
        
            

class Horse:
    def __init__(self, teamId, shape):
        self.teamId = teamId
        self.shape = shape
        self.numberOfTileCrossed = 0
        self.currentTileIndex = -1
        self.Finished = False
