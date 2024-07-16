from tkinter import *
from PIL import Image,ImageTk
import random
def dice():
    choose1 = random.choice(images)
    img00 = Image.open(choose1)
    img10 = ImageTk.PhotoImage(img00)
    dice1.config(image=img10)
    dice1.image = img10
    choose2 = random.choice(images)
    img20 = Image.open(choose2)
    img30 = ImageTk.PhotoImage(img20)
    dice2.config(image=img30)
    dice2.image = img30
root = Tk()
root.title('Dice Roller')
root.resizable(0,0)
root.config(bg='black')
root.geometry('650x500+350+100')
images = ['1.png','2.png','3.jpeg','4.jpeg','5.jpeg','6.png']
pic = random.choice(images)
img0 = Image.open(pic)
img1 = ImageTk.PhotoImage(img0)
dice1 = Label(root,image=img1,bd=0)
dice1.place(x=40,y=130)
pic1 = random.choice(images)
img2 = Image.open(pic1)
img3 = ImageTk.PhotoImage(img2)
dice2 = Label(root,image=img3,bd=0)
dice2.place(x=370,y=130)
roll = Button(root,text='Roll',font='Times 15 bold',fg='#000',bg='#ea3548',
              padx=20,pady=2,bd=2,activebackground='silver',activeforeground='#000',command=dice,relief=GROOVE)
roll.pack(padx=2,pady=10,side=TOP)
root.mainloop()