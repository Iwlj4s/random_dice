import random
from tkinter import *

root = Tk()

root.title('Random Dice Roller')  # Window Settings
root.geometry('765x305')
root.resizable(width=False, height=False)
root['background'] = '#9e9c72'

root.iconbitmap(r'C:\Users\Iwlj4s\Desktop\pm\random_dice\img\logo.ico')

l1 = Label(root, font=('consolas', 200))  # Label for dice
l2 = Label(root, font=('consolas', 200))


def roll_single():  # Function for single Roll
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f"{random.choice(number)}")
    l1['background'] = '#9e9c72'
    l2.pack_forget()
    l1.pack()


def roll_twice():  # Function for Twice roll
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l2.config(text=f"{random.choice(number)}{random.choice(number)}")
    l2['background'] = '#9e9c72'
    l1.pack_forget()
    l2.pack()


# First button settings
b1 = Button(root, text='Roll Single', width=10, height=2, bg='white', command=roll_single)
b1.place(x=124, y=0)
b1['border'] = '1'
# Second button settings
b2 = Button(root, text='Roll Twice', width=10, height=2,  bg='white', command=roll_twice)
b2.place(x=554, y=0)
b1['border'] = '1'

root.mainloop()
