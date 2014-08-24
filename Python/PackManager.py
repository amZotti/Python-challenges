from tkinter import *

class PackManagerDemo:
    def __init__(self):
        main_container = Tk()
        main_container.title("PAck manager demo1")











        Label(main_container, bg = "blue", text = "Blue").pack()
        Label(main_container,  bg = "red", text= "Red").pack(fill = Y, expand = 1)
        Label(main_container, text="Green", bg = "green").pack(
            fill = X)
        main_container.mainloop()

PackManagerDemo()
        
        
