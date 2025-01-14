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
    #endregion Draw players camps

    #region Draw main locations
    for i in range(15): 
        if(i != 7):
            if(i == 0):
                canvas.create_oval(locationSize * i + borderSize, locationSize * 6 + borderSize, locationSize * i + locationDisplaySize, locationSize * 6 + locationDisplaySize, fill=redLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * i + borderSize, locationSize * 6 + borderSize, locationSize * i + locationDisplaySize, locationSize * 6 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
            if(i == 14):
                canvas.create_oval(locationSize * i + borderSize, locationSize * 8 + borderSize, locationSize * i + locationDisplaySize, locationSize * 8 + locationDisplaySize, fill=yellowLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * i + borderSize, locationSize * 8 + borderSize, locationSize * i + locationDisplaySize, locationSize * 8 + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    
    for i in range(15): 
        if(i != 7):
            if(i == 14):
                canvas.create_oval(locationSize * 6 + borderSize, locationSize * i + borderSize, locationSize * 6 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=blueLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * 6 + borderSize, locationSize * i + borderSize, locationSize * 6 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=bgColor, outline=bgColorBis)
            if(i == 0):
                canvas.create_oval(locationSize * 8 + borderSize, locationSize * i + borderSize, locationSize * 8 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=greenLocationColors, outline=bgColorBis)
            else:
                canvas.create_oval(locationSize * 8 + borderSize, locationSize * i + borderSize, locationSize * 8 + locationDisplaySize, locationSize * i + locationDisplaySize, fill=bgColor, outline=bgColorBis)
    
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


isRunning = True

DrawBoard()
root.mainloop()

# while(isRunning):
    


#     #CODE MUST BE HIGHER THAN THIS
#     root.mainloop()