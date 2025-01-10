# Only for shared logics and UIs

import logics
import tkinter as tk
from tkinter import *

root = tk.Tk()

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
    canvas.create_rectangle(0, 0, locationSize*6 - borderSize, locationSize*6 - borderSize, fill="red", outline="gray35")
    canvas.create_rectangle(0, size, locationSize*6 - borderSize, size + borderSize - locationSize*6, fill="blue", outline="gray35")
    canvas.create_rectangle(size + borderSize - locationSize*6, 0, size, locationSize*6 - borderSize, fill="green", outline="gray35")
    canvas.create_rectangle(size + borderSize - locationSize*6, size + borderSize - locationSize*6, size, size, fill="yellow", outline="gray35")
    #endregion Draw players camps

    #region Draw main locations
    for i in range(15): 
        if(i != 7):
            canvas.create_oval(locationSize * i + borderSize, locationSize * 6 + borderSize, locationSize * i + locationDisplaySize, locationSize * 6 + locationDisplaySize, fill="gray20", outline='gray35')
            canvas.create_oval(locationSize * i + borderSize, locationSize * 8 + borderSize, locationSize * i + locationDisplaySize, locationSize * 8 + locationDisplaySize, fill="gray20", outline='gray35')
    
    for i in range(15): 
        if(i != 7):
            canvas.create_oval(locationSize * 6 + borderSize, locationSize * i + borderSize, locationSize * 6 + locationDisplaySize, locationSize * i + locationDisplaySize, fill="gray20", outline='gray35')
            canvas.create_oval(locationSize * 8 + borderSize, locationSize * i + borderSize, locationSize * 8 + locationDisplaySize, locationSize * i + locationDisplaySize, fill="gray20", outline='gray35')
    
    canvas.create_oval(locationSize * 0 + borderSize, locationSize * 7 + borderSize, locationSize * 0 + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill="gray20", outline='gray35')
    canvas.create_oval(locationSize * 7 + borderSize, locationSize * 14 + borderSize, locationSize * 7 + locationDisplaySize, locationSize * 14 + locationDisplaySize, fill="gray20", outline='gray35')
    canvas.create_oval(locationSize * 7 + borderSize, locationSize * 0 + borderSize, locationSize * 7 + locationDisplaySize, locationSize * 0 + locationDisplaySize, fill="gray20", outline='gray35')
    canvas.create_oval(locationSize * 14 + borderSize, locationSize * 7 + borderSize, locationSize * 14 + locationDisplaySize, locationSize * 7 + locationDisplaySize, fill="gray20", outline='gray35')
    #endregion Draw main locations

    # Update Canvas
    canvas.pack()

#endregion UI Method Related


isRunning = True

DrawBoard()
root.mainloop()

# while(isRunning):
    


#     #CODE MUST BE HIGHER THAN THIS
#     root.mainloop()