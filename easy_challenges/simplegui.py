from tkinter import *

class SampleGUI:
    def __init__(self):
        self.count = 0
        self.window = Tk()
        self.button = Button(self.window,
                             text = 'Add',
                             fg = 'red',
                             command = self.do_button)
        self.button['bg'] = '#FFFF00'
        self.button.pack()
        self.label = Label(self.window,
                           text = "0")
        self.label.pack()
        self.window.mainloop()

    def do_button(self):
        self.count += 1
        self.label['text'] = str(self.count)

SampleGUI()
        
        
