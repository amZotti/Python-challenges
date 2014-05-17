import random
from tkinter import *


class histogram:
    def __init__(self,count,alphabet):
        self.count = count
        self.alphabet = alphabet

        window = Tk()
        window.title("Count of Each Letter")
        self.canvas = Canvas(window, width=550,height=400,bg='white')
        self.canvas.pack()
        self.drawRectangle()
        self.draw_alphabet()
        window.mainloop()

        


    def drawRectangle(self):
        #x pos must move up in 20 unit increments because that is width
        x_pos = 20
        x_pos2 = 40
        height = 200


        
        for i in self.count:
            height = i * 5
            self.canvas.create_rectangle(x_pos,350,x_pos2,height,tags='rect')
            x_pos += 20
            x_pos2 += 20

    def draw_alphabet(self):
        x_pos = 30
        y_pos = 360


        for k in self.alphabet:
            self.canvas.create_text(x_pos,y_pos,text=str(k))
            x_pos+=20
            
        
        
        
        

def generateRandomLetters():
    letters = ''
    for i in range(1000):
        letters += chr(random.randint(97,122))


    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    count = []
    for i in alphabet:
        count.append(letters.count(i))

    return count, alphabet

def main():
    count,alphabet = generateRandomLetters()
    histogram(count,alphabet)












    


if __name__ == "__main__":
    main()



    
        
        
