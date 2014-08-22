from tkinter import *

class box:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas = Canvas(window, width = 400, height = 100, bg = 'white')
        self.canvas.pack()
        

        frame = Frame(window)
        frame.pack()
        frame2 = Frame(window)
        frame2.pack()

        self.v1 = IntVar()
        self.v2 = IntVar()
        cbtFilled = Checkbutton(frame2,text= "Filled",variable = self.v2, command = self.processCheckButton).pack(side=RIGHT)
        rbRect = Radiobutton(frame2, text = "Rectangle", variable = self.v1, value = 1, command = self.processRadiobutton).pack(side=LEFT)
        rbOval = Radiobutton(frame2, text = "Oval", variable = self.v1, value = 2, command = self.processRadiobutton).pack(side = RIGHT)
        window.mainloop()
    def processCheckButton(self):
        if self.v2.get() == 1:
            self.canvas.itemconfigure(self.item,fill='black')
        else:
            
            self.canvas.itemconfigure(self.item,fill='white')

    def processRadiobutton(self):
        if self.v1.get() == 1:
            self.drawRectangle()
        else:
            self.drawOval()

    def drawRectangle(self):
        self.clearCanvas()
        
        
        self.item=self.canvas.create_rectangle(35, 10 ,350,90,tags = 'rect')
        self.processCheckButton()

    def drawOval(self):
        self.clearCanvas()
        
        
        self.item=self.canvas.create_oval(50, 10, 350, 100, tags = 'oval')
        self.processCheckButton()

    def clearCanvas(self):
        self.canvas.delete('rect','oval')
        
        
def main():
    box()

if __name__ == "__main__":
    main()

