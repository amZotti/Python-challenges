from tkinter import *

class grid:
    def __init__(self):
        window = Tk()
        window.title("Grid")
        
        self.canvas = Canvas(window, width = 238,height = 238, bg = 'white')
        self.canvas.pack()
        self.displayYLines()
        self.displayXlines()
        window.mainloop()
      


    def displayYLines(self):
        Y_START = 0
        Y_END = 300
        x = 0
        for i in range(8):
            
            x += 30
            self.canvas.create_line(x,Y_START,x,Y_END,fill='red')

    def displayXlines(self):
        X_START = 0
        X_END = 300
        y = 0
        for i in range(8):
            
            y += 30
            self.canvas.create_line(X_START,y,X_END,y,fill='blue')


def main():
    grid()      

if __name__ == "__main__":
    main()
