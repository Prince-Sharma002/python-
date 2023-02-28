from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

r = Tk()
r.geometry("600x400")
r.title("Notepad")

def fun():
    pass


#Scroll bar and Text Area
scroll  = Scrollbar(r)
scroll.pack(fill = "y" , side = RIGHT )
t = Text(r , yscrollcommand = scroll.set)
t.pack(fill = "both")
scroll.config(command = t.yview)

#Edit Functions
def cut():
    t.event_generate(("<<Cut>>"))
def copy():
    t.event_generate(("<<Copy>>"))
def paste():
    t.event_generate(("<<Paste>>"))
def Help():
    tmsg.showinfo("ABOUT" , "This is Prince Notepad")
def new():
    global file
    r.title("Untitled-Notepad")
    file = None
    t.delete(1.0 , END) #1.0 means first line first character - delete till end

def open():
    global file
    file = askopenfilename(defaultextension = ".txt" , filetypes =
    [("All Files" , "*.*") ,
    ("Text Documents" , "*.txt")]) # (.* - all files) (.txt - only txt files)

    if file == "":
        file = None
    else:
        r.title(os.path.basename(file) + "-Notepad") #change name of file in tkinter
        t.delete(1.0 , END)
        with open(file , "r") as g:
            t.insert(1.0 , g)
            g.close()




#Main Menu Starts
mainMenu = Menu(r)

#FILE MENU STARTS
fileMenu = Menu(mainMenu , tearoff = 0)
fileMenu.add_command(label = "NEW" , command = new)
fileMenu.add_command(label = "OPEN" , command = open)
fileMenu.add_command(label = "SAVE" , command = fun)
fileMenu.add_command(label = "EXIT" , command = fun)
mainMenu.add_cascade(label = "FILE" , menu = fileMenu)

#EDITMENU STARTS
editMenu = Menu(mainMenu , tearoff = 0)
editMenu.add_command(label = "CUT" , command = cut)
editMenu.add_command(label = "COPY" , command = copy)
editMenu.add_command(label = "PASTE" , command = paste)
mainMenu.add_cascade(label = "EDIT" , menu = editMenu)

#HELPMENU STARTS
helpMenu = Menu(mainMenu , tearoff = 0)
helpMenu.add_command(label = "About Notepad" ,command = Help)
mainMenu.add_cascade(label = "HELP" , menu = helpMenu)





r.config(menu = mainMenu)




r.mainloop()