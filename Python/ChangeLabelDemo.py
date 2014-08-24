from tkinter import *

class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Hex converter")

        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Welcome comrade!")
        self.lbl.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter numbers: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "Convert",
                              command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Hex to Dec",
                            variable = self.v1, value = "R")
        rbYellow = Radiobutton(frame2, text = "Dec to Hex",
                            variable = self.v1, value = "Y")

        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        

        window.mainloop()



    def processButton(self):
        self.lbl['fg']='black'
        num=self.msg.get()
        try:
            if self.v1.get() == "R":
                mystr=str(int(num, 16))
                
                self.lbl['text'] = mystr
                      
            else:
                mystr = str(hex(int(num)))
                self.lbl['text'] = mystr
        except Exception:
            self.lbl['fg']='red'
            self.lbl['text']="Invalid number for conversion!"
            
def main():
    ChangeLabelDemo()
if __name__ == "__main__":
    main()
