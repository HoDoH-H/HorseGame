# Only for shared logics and UIs

import logics
import tkinter as tk
from tkinter import *

root = tk.Tk()

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

size = 750
locationSize = size/15
borderSize = 5
locationDisplaySize = locationSize-borderSize

canvas = Canvas(root, width=size, height=size, background=GlobalbgColor)
canvas.pack()

#endregion Main Page Setter

#region UI Method Related

def DrawBoard():
    """
    Used to draw the board on the root windows inside a canvas
    """
    #region Draw players camps
    canvas.create_rectangle(3, 3, locationSize*6, locationSize*6, fill=redLocationColors, outline=bgColorBis)
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

#endregion UI Method Related

def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      if(x < locationSize*6):
          canvas.coords(horses[0][0].shape, locationSize * 0 + borderSize, locationSize * 7 + borderSize, locationSize * 0 + locationDisplaySize, locationSize * 7 + locationDisplaySize)
          canvas.update()
          

isRunning = True

DrawBoard()
root.bind("<Button 1>",getorigin)

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