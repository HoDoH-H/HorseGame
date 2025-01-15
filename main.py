# Only for shared logics and UIs

import logics
import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
turn = 0
turnValue = 1

#region Colors
GlobalbgColor = "gray0"
bgColor = "gray18"
bgColorBis = "gray5"

redColor = "firebrick4"
redLocationColors = "firebrick2"
greenColor = "SpringGreen4"
greenLocationColors = "SpringGreen2"
yellowColor = "gold4"
yellowLocationColors = "gold2"
blueColor = "RoyalBlue4"
blueLocationColors = "RoyalBlue2"
#endregion Colors

#region Main Page Setter

size = logics.size
locationSize = logics.locationSize
borderSize = logics.borderSize
locationDisplaySize = logics.locationDisplaySize

canvas = Canvas(root, width=size, height=size, background=GlobalbgColor)
canvas.pack()

#endregion Main Page Setter

#region UI Method Related

def DrawBoard():
    """
    Used to draw the board on the root windows inside a canvas
    """
    #region Draw players camps
    canvas.create_rectangle(3, 3, locationSize*6, locationSize*6, fill=redLocationColors, outline=bgColorBis, tags="RedCamp")
    canvas.create_rectangle(3, size, locationSize*6, size - locationSize*6, fill=blueLocationColors, outline=bgColorBis)
    canvas.create_rectangle(size - locationSize*6, 3, size, locationSize*6, fill=greenLocationColors, outline=bgColorBis)
    canvas.create_rectangle(size - locationSize*6, size - locationSize*6, size, size, fill=yellowLocationColors, outline=bgColorBis)

    for t in range(4):
        for h in range(4):
            canvas.create_oval(locationSize * logics.playerCampsPos[t][h][0] + borderSize, locationSize * logics.playerCampsPos[t][h][1] + borderSize, locationSize * logics.playerCampsPos[t][h][0] + locationDisplaySize, locationSize * logics.playerCampsPos[t][h][1] + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    #endregion Draw players camps

    #region Draw main locations
    for i in range(15): 
        if(i != 7):
            if(i == 0):
                canvas.create_oval(locationSize * i + borderSize, locationSize * 6 + borderSize, locationSize * i + locationDisplaySize, locationSize * 6 + locationDisplaySize, fill=redLocationColors, outline=bgColorBis)
                canvas.create_oval(locationSize * 8 + borderSize, locationSize * i + borderSize, locationSize * 8 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=greenLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * i + borderSize, locationSize * 6 + borderSize, locationSize * i + locationDisplaySize, locationSize * 6 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
                canvas.create_oval(locationSize * 8 + borderSize, locationSize * i + borderSize, locationSize * 8 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=bgColor, outline=bgColorBis)
            if(i == 14):
                canvas.create_oval(locationSize * i + borderSize, locationSize * 8 + borderSize, locationSize * i + locationDisplaySize, locationSize * 8 + locationDisplaySize, fill=yellowLocationColors, outline=bgColorBis)
                canvas.create_oval(locationSize * 6 + borderSize, locationSize * i + borderSize, locationSize * 6 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=blueLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * i + borderSize, locationSize * 8 + borderSize, locationSize * i + locationDisplaySize, locationSize * 8 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
                canvas.create_oval(locationSize * 6 + borderSize, locationSize * i + borderSize, locationSize * 6 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=bgColor, outline=bgColorBis)
                
    
    canvas.create_oval(locationSize * 0 + borderSize, locationSize * 7 + borderSize, locationSize * 0 + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    canvas.create_oval(locationSize * 7 + borderSize, locationSize * 14 + borderSize, locationSize * 7 + locationDisplaySize, locationSize * 14 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    canvas.create_oval(locationSize * 7 + borderSize, locationSize * 0 + borderSize, locationSize * 7 + locationDisplaySize, locationSize * 0 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    canvas.create_oval(locationSize * 14 + borderSize, locationSize * 7 + borderSize, locationSize * 14 + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    #endregion Draw main locations

    #region Draw ladders
    for i in range(1, 7):
        canvas.create_rectangle(locationSize * i + borderSize, locationSize * 7 + borderSize, locationSize * i + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill=redLocationColors, outline=bgColorBis)
        canvas.create_rectangle(locationSize * (i + 7) + borderSize, locationSize * 7 + borderSize, locationSize * (i + 7) + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill=yellowLocationColors, outline=bgColorBis)

    for i in range(1, 7):
        canvas.create_rectangle(locationSize * 7 + borderSize, locationSize * i + borderSize, locationSize * 7 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=greenLocationColors, outline=bgColorBis)
        canvas.create_rectangle(locationSize * 7 + borderSize, locationSize * (i + 7) + borderSize, locationSize * 7 + locationDisplaySize, locationSize * (i + 7) + locationDisplaySize, fill=blueLocationColors, outline=bgColorBis)

    canvas.create_polygon([locationSize * 7 + locationSize/2, locationSize * 8 - locationSize/2, locationSize * 7 + borderSize, locationSize * 8 - borderSize, locationSize * 8 - borderSize, locationSize * 8 - borderSize], fill=blueLocationColors)
    canvas.create_polygon([locationSize * 7 + locationSize/2, locationSize * 8 - locationSize/2, locationSize * 7 + borderSize, locationSize * 7 + borderSize, locationSize * 8 - borderSize, locationSize * 7 + borderSize], fill=greenLocationColors)
    canvas.create_polygon([locationSize * 7 + locationSize/2, locationSize * 8 - locationSize/2, locationSize * 7 + borderSize, locationSize * 8 - borderSize, locationSize * 7 + borderSize, locationSize * 7 + borderSize], fill=redLocationColors)
    canvas.create_polygon([locationSize * 7 + locationSize/2, locationSize * 8 - locationSize/2, locationSize * 8 - borderSize, locationSize * 8 - borderSize, locationSize * 8 - borderSize, locationSize * 7 + borderSize], fill=yellowLocationColors)
    #endregion Draw ladders

    # Update Canvas
    canvas.pack()


def CanvasClicked(event):
    global x,y, turnValue, turn
    x = event.x
    y = event.y

    print("Turn when clicked: ", turn)

    #turnValue = random.randint(1, 6)
    
    # Check if current player click on a camp
    if(x < locationSize*6 and y < locationSize*6 and turn == 0):
        getHorseOutOfCamp(0)
    elif(x > locationSize*9 and y < locationSize*6 and turn == 1):
        getHorseOutOfCamp(1)
    elif(x > locationSize*9 and y > locationSize*9 and turn == 2):
        getHorseOutOfCamp(2)
    elif(x < locationSize*6 and y > locationSize*9 and turn == 3):
        getHorseOutOfCamp(3)
    else: # Check if current player click on a location
        TryMoveHorse()

#endregion UI Method Related

def TryMoveHorse():
    for h in range(4):
        if(horses[turn][h].Finished == False and horses[turn][h].currentTileIndex != -1):
            if(logics.locationsPos[horses[turn][h].currentTileIndex][0] * locationSize < x < (logics.locationsPos[horses[turn][h].currentTileIndex][0] + 1) * locationSize and logics.locationsPos[horses[turn][h].currentTileIndex][1] * locationSize < y < (logics.locationsPos[horses[turn][h].currentTileIndex][1] + 1) * locationSize):
                notc = horses[turn][h].numberOfTileCrossed + turnValue - 56
                ct = horses[turn][h].currentTileIndex + turnValue - 56
                if(horses[turn][h].currentTileIndex >= 56): # If horse is in the ladder
                    if(horses[turn][h].currentTileIndex + turnValue > logics.teamLadderStart[turn] + 6): # Can't move more than the size of the ladder
                        return
                    elif(horses[turn][h].currentTileIndex + turnValue == logics.teamLadderStart[turn] + 6): # Makes horse disapear if it reaches just the size of the ladder
                        horses[turn][h].Finished, horses[turn][h].currentTileIndex = True, -2
                        canvas.coords(horses[turn][h].shape, 0, 0, 0, 0)
                    else: # Move the horse on the ladder
                        if(checkIfTileEmpty(horses[turn][h].currentTileIndex + turnValue)):
                            horses[turn][h].numberOfTileCrossed += turnValue
                            moveHorse(horses[turn][h], horses[turn][h].currentTileIndex + turnValue)
                elif(horses[turn][h].numberOfTileCrossed + turnValue >= 56): # If horse need to start climbing the ladder
                    if(checkIfTileEmpty(logics.teamLadderStart[turn] + notc)):
                        horses[turn][h].numberOfTileCrossed += turnValue
                        moveHorse(horses[turn][h], logics.teamLadderStart[turn] + notc)
                elif(horses[turn][h].currentTileIndex + turnValue >= 56): # If horse need to get to the first tile
                    if(checkIfTileEmpty(ct)):
                        horses[turn][h].numberOfTileCrossed += turnValue
                        moveHorse(horses[turn][h], ct)
                elif(checkIfTileEmpty(horses[turn][h].currentTileIndex + turnValue)): # If horse doesn't need anything special, just go
                    horses[turn][h].numberOfTileCrossed += turnValue
                    moveHorse(horses[turn][h], horses[turn][h].currentTileIndex + turnValue)

def checkIfTileEmpty(tile):
    for t in range(4):
        for h in range(4):
            if(horses[t][h].currentTileIndex == tile):
                if(turn == t): # If there's a horse of the same team
                    return False
                else: # If there's a horse from another team
                    # TODO - Make enemy horse get back to its camp
                    return True
    return True

def getHorseOutOfCamp(teamId):
    if(checkIfTileEmpty(logics.teamSpawns[teamId])):
        for i in range(4):
            if(horses[teamId][i].currentTileIndex == -1):
                moveHorse(horses[teamId][i], logics.teamSpawns[teamId])
                horses[teamId][i].numberOfTileCrossed = 0
                return
            
def getHorseBackToCamp(horse : logics.Horse):
    horse.currentTileIndex, horse.numberOfTileCrossed = 0, 0
    
                

def moveHorse(horse : logics.Horse, location, passTurn = True):
    global turn

    horse.currentTileIndex = location
    canvas.coords(horse.shape, locationSize * logics.locationsPos[location][0] + borderSize, locationSize * logics.locationsPos[location][1] + borderSize, locationSize * logics.locationsPos[location][0] + locationDisplaySize, locationSize * logics.locationsPos[location][1] + locationDisplaySize)
    if(passTurn):
        turn = logics.RunTurns(turn, horses)

isRunning = True

DrawBoard()
canvas.bind("<Button 1>",CanvasClicked)

horses = [[logics.Horse(0, canvas.create_oval(locationSize * logics.playerCampsPos[0][0][0] + borderSize, locationSize * logics.playerCampsPos[0][0][1] + borderSize, locationSize * logics.playerCampsPos[0][0][0] + locationDisplaySize, locationSize * logics.playerCampsPos[0][0][1] + locationDisplaySize, fill=redColor, outline=bgColorBis)), 
           logics.Horse(0, canvas.create_oval(locationSize * logics.playerCampsPos[0][1][0] + borderSize, locationSize * logics.playerCampsPos[0][1][1] + borderSize, locationSize * logics.playerCampsPos[0][1][0] + locationDisplaySize, locationSize * logics.playerCampsPos[0][1][1] + locationDisplaySize, fill=redColor, outline=bgColorBis)), 
           logics.Horse(0, canvas.create_oval(locationSize * logics.playerCampsPos[0][2][0] + borderSize, locationSize * logics.playerCampsPos[0][2][1] + borderSize, locationSize * logics.playerCampsPos[0][2][0] + locationDisplaySize, locationSize * logics.playerCampsPos[0][2][1] + locationDisplaySize, fill=redColor, outline=bgColorBis)), 
           logics.Horse(0, canvas.create_oval(locationSize * logics.playerCampsPos[0][3][0] + borderSize, locationSize * logics.playerCampsPos[0][3][1] + borderSize, locationSize * logics.playerCampsPos[0][3][0] + locationDisplaySize, locationSize * logics.playerCampsPos[0][3][1] + locationDisplaySize, fill=redColor, outline=bgColorBis))], #Red team
          
          [logics.Horse(1, canvas.create_oval(locationSize * logics.playerCampsPos[1][0][0] + borderSize, locationSize * logics.playerCampsPos[1][0][1] + borderSize, locationSize * logics.playerCampsPos[1][0][0] + locationDisplaySize, locationSize * logics.playerCampsPos[1][0][1] + locationDisplaySize, fill=greenColor, outline=bgColorBis)), 
           logics.Horse(1, canvas.create_oval(locationSize * logics.playerCampsPos[1][1][0] + borderSize, locationSize * logics.playerCampsPos[1][1][1] + borderSize, locationSize * logics.playerCampsPos[1][1][0] + locationDisplaySize, locationSize * logics.playerCampsPos[1][1][1] + locationDisplaySize, fill=greenColor, outline=bgColorBis)), 
           logics.Horse(1, canvas.create_oval(locationSize * logics.playerCampsPos[1][2][0] + borderSize, locationSize * logics.playerCampsPos[1][2][1] + borderSize, locationSize * logics.playerCampsPos[1][2][0] + locationDisplaySize, locationSize * logics.playerCampsPos[1][2][1] + locationDisplaySize, fill=greenColor, outline=bgColorBis)), 
           logics.Horse(1, canvas.create_oval(locationSize * logics.playerCampsPos[1][3][0] + borderSize, locationSize * logics.playerCampsPos[1][3][1] + borderSize, locationSize * logics.playerCampsPos[1][3][0] + locationDisplaySize, locationSize * logics.playerCampsPos[1][3][1] + locationDisplaySize, fill=greenColor, outline=bgColorBis))], #Green team
          
          [logics.Horse(2, canvas.create_oval(locationSize * logics.playerCampsPos[2][0][0] + borderSize, locationSize * logics.playerCampsPos[2][0][1] + borderSize, locationSize * logics.playerCampsPos[2][0][0] + locationDisplaySize, locationSize * logics.playerCampsPos[2][0][1] + locationDisplaySize, fill=yellowColor, outline=bgColorBis)), 
           logics.Horse(2, canvas.create_oval(locationSize * logics.playerCampsPos[2][1][0] + borderSize, locationSize * logics.playerCampsPos[2][1][1] + borderSize, locationSize * logics.playerCampsPos[2][1][0] + locationDisplaySize, locationSize * logics.playerCampsPos[2][1][1] + locationDisplaySize, fill=yellowColor, outline=bgColorBis)), 
           logics.Horse(2, canvas.create_oval(locationSize * logics.playerCampsPos[2][2][0] + borderSize, locationSize * logics.playerCampsPos[2][2][1] + borderSize, locationSize * logics.playerCampsPos[2][2][0] + locationDisplaySize, locationSize * logics.playerCampsPos[2][2][1] + locationDisplaySize, fill=yellowColor, outline=bgColorBis)), 
           logics.Horse(2, canvas.create_oval(locationSize * logics.playerCampsPos[2][3][0] + borderSize, locationSize * logics.playerCampsPos[2][3][1] + borderSize, locationSize * logics.playerCampsPos[2][3][0] + locationDisplaySize, locationSize * logics.playerCampsPos[2][3][1] + locationDisplaySize, fill=yellowColor, outline=bgColorBis))], #Yellow team
          
          [logics.Horse(3, canvas.create_oval(locationSize * logics.playerCampsPos[3][0][0] + borderSize, locationSize * logics.playerCampsPos[3][0][1] + borderSize, locationSize * logics.playerCampsPos[3][0][0] + locationDisplaySize, locationSize * logics.playerCampsPos[3][0][1] + locationDisplaySize, fill=blueColor, outline=bgColorBis)), 
           logics.Horse(3, canvas.create_oval(locationSize * logics.playerCampsPos[3][1][0] + borderSize, locationSize * logics.playerCampsPos[3][1][1] + borderSize, locationSize * logics.playerCampsPos[3][1][0] + locationDisplaySize, locationSize * logics.playerCampsPos[3][1][1] + locationDisplaySize, fill=blueColor, outline=bgColorBis)), 
           logics.Horse(3, canvas.create_oval(locationSize * logics.playerCampsPos[3][2][0] + borderSize, locationSize * logics.playerCampsPos[3][2][1] + borderSize, locationSize * logics.playerCampsPos[3][2][0] + locationDisplaySize, locationSize * logics.playerCampsPos[3][2][1] + locationDisplaySize, fill=blueColor, outline=bgColorBis)), 
           logics.Horse(3, canvas.create_oval(locationSize * logics.playerCampsPos[3][3][0] + borderSize, locationSize * logics.playerCampsPos[3][3][1] + borderSize, locationSize * logics.playerCampsPos[3][3][0] + locationDisplaySize, locationSize * logics.playerCampsPos[3][3][1] + locationDisplaySize, fill=blueColor, outline=bgColorBis))]] #Blue team



root.mainloop()