import random
import string
from tkinter import *
from tkinter import ttk

root = Tk()  
root.geometry('250x150')  
root.title('Password Generator by Todo')

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def passgen():

    random.shuffle(characters)

    password = []
    for i in range(length.get()):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

lengthLabel = Label(root, text="Password length:").grid(row=0, column=0)
length = IntVar()
lengthEntry = Entry(root, textvariable=length).grid(row=0, column=1)

GenButton = Button(root, text="Generate", command=passgen).grid(row=1, column=0) 

root.mainloop()