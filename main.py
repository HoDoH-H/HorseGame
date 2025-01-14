# Only for shared logics and UIs

import logics
import tkinter as tk
from tkinter import *

root = tk.Tk()

#region Colors
bgColor = "gray20"
bgColorBis = "gray35"

redColor = "red"
redLocationColors = "red4"
greenColor = "green"
greenLocationColors = "green4"
yellowColor = "yellow"
yellowLocationColors = "goldenrod"
blueColor = "blue"
blueLocationColors = "blue4"
#endregion Colors

#region Main Page Setter

size = 900
locationSize = size/15
borderSize = 5
locationDisplaySize = locationSize-borderSize

canvas = Canvas(root, width=size, height=size, background="gray35")
canvas.pack()

#endregion Main Page Setter

#region UI Method Related

def DrawBoard():
    """
    Used to draw the board on the root windows inside a canvas
    """
    #region Draw players camps
    canvas.create_rectangle(0, 0, locationSize*6 - borderSize, locationSize*6 - borderSize, fill=redLocationColors, outline=bgColorBis)
    canvas.create_rectangle(0, size, locationSize*6 - borderSize, size + borderSize - locationSize*6, fill=blueLocationColors, outline=bgColorBis)
    canvas.create_rectangle(size + borderSize - locationSize*6, 0, size, locationSize*6 - borderSize, fill=greenLocationColors, outline=bgColorBis)
    canvas.create_rectangle(size + borderSize - locationSize*6, size + borderSize - locationSize*6, size, size, fill=yellowLocationColors, outline=bgColorBis)
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