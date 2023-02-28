import wsgiref.validate
from tkinter import *
from PIL import ImageTk , Image
import tkinter.messagebox as tmsg


"""
root = Tk()

a  =  Entry(root , bg = "red" , borderwidth = 5 , width = 50)
a.pack()
a.insert(10 , "enetr your name")

def fu():
    myLabel = Label(root , text = "heloo    " + a.get())
    myLabel.pack()

mybut = Button(root , text = "Enter your name" , command= fu , bg = 'red')
mybut.pack()

root.mainloop()
"""


"""
#inserting icon , image, title ,quit button
r = Tk()
r.title("practice of title and icon")
r.iconbitmap("D:\python\Python Projects\Tinkter\Dakirby309-Windows-8-Metro-Apps-Calculator-Metro.ico")

quit_button  = Button(r , text = "quit" , command = r.quit)
quit_button.pack()

#for png formate
i = PhotoImage(file = "")

# for jpg formate
my_img = ImageTk.PhotoImage(Image.open(""))
my_label = Label(image = my_img)
my_label.pack()

r.mainloop()
"""



"""
#geometry ( width x height )
r  = Tk()

#widthxheight
r.geometry("300x200")

#width , height
r.minsize(200, 200)
r.maxsize(400, 400)


r.title("geometry")

r.mainloop()
"""

"""
#Label
r = Tk()
r.geometry("500x500")
r.title("Label")
l = Label(r , text ="Abdul Rashid Salim Salman Khan \n(Hindi: [səlˈmɑːn xɑːn]; 27 "
                    "December 1965)[2] is an Indian actor, film producer \n , and television "
                    "personality who works in Hindi films. In a film career spanning over thirty years,"
                    " Khan has received \nnumerous awards, including two National Film Awards as a film "
                    "producer, and two Filmfare Awa\nrds as an actor.[3] He is cited in the media as one of "
                    "the most commercially successful actors of Indian\n cinema.[4][5] Forbes included him "
                    "in their 2015 list of Top-Paid 100 \nCelebrity Entertainers in the world; Khan tied with"
                    " Amitabh Bachchan for No. 71 on th\ne list, both with earnings of $33.5 million.[6][7]"
                    " According to the Forbes 2018 list\n of Top-Paid 100 Celebrity Entertainers in world, "
                    "Khan was the highest-ranked \nIndian with 82nd rank with earnings of $37.7 million."
                    "[8][9] He has also been hosting the \nreality show, Bigg Boss since 2010." ,
          bg ="red" , pady = 0  , fg = "white" , font =("comicsanms" , 6 , "bold" ) , borderwidth = 10,
          relief = GROOVE )
#SUNKEN , RAISED , GROOVE , RIDGE

#PACKING
#l.pack( anchor = "nw") #northwest

#for bottom sw or se
#l.pack(side = BOTTOM , anchor = "se")

#fill FOR Y
#l.pack(side = LEFT , fill = Y)

#PADDING IN PACKING - for moving label
#l.pack(padx  = 20 , pady  = 200)

r.mainloop()
"""




"""
#CHALLANGE OF MAKING OF STRIP IN BOTTOM
r = Tk()

r.geometry("500x400")
l = Label(r , text = "READY" , bg ="red" , fg = "white")
l.pack(side = BOTTOM , fill = X)

r.mainloop()
"""


"""
#PHOTO RESIZER
r = Tk()

r.title("BIO=DATA")

i = Image.open("me2.png")
im = i.resize((500, 500))
img  = ImageTk.PhotoImage(im)

l3 = Label(r , text = "PRINCE SHARMA" , font = ("comicsanms" , 10 , "bold") , padx =200)
l3.grid(pady = 20)
l2 = Label(r , text = "Class : 12TH \nDOB : 12-08-2004 \nFathers Name : Pawan Sharma \nMothers Name : Sunita Sharma")
l2.grid(row = 1 , column  = 0 , padx = 200 )

l = Label(r , image = img)
l.grid(row = 1 , column = 1 )

r.mainloop()
"""


r  = Tk()



"""
#FRAME
r.geometry("500x400")

f1 = Frame(r , bg = "grey" , borderwidth  =5)
f2 = Frame(r , bg = "red" , borderwidth = 10)
l1 = Label(f1 , text = "hello" , padx = 40 , pady =600)
l2 = Label(f2 , text = "BIO-DATA" , padx = 600 , pady = 20)

f1.pack(side = LEFT , fill = "y" , pady =200)
f2.pack(side = TOP , fill = "x")
l1.pack(pady = 100)
l2.pack()
"""




#BUTTON
"""
r.geometry("500x500")
f1 = Frame(r , bg = "red" , borderwidth = 5 ,relief = SUNKEN  )
b1 = Button(f1 , text = "CLICK ME1")
b2 = Button(f1 , text = "CLICK ME2")
b3 = Button(f1 , text = "CLICK ME3")

f1.pack(anchor = "nw")
b1.pack(side = LEFT , padx = 20)
b2.pack(side = RIGHT, padx = 20)
b3.pack(side = RIGHT , padx = 20)
"""

#ENTRY WITH USING INSERT NAME FORM
""""
def entry():
    print(f"name is {uservalue.get()}")

r.geometry("500x500")

f1  = Frame(r, borderwidth = 5 , bg = "red" , relief = SUNKEN)
uservalue = StringVar()
e1 = Entry(f1 , textvariable = uservalue , relief = SUNKEN , borderwidth = 5)

f1.pack(side = TOP , fill = "x")
e1.pack(pady = 10)

b1 = Button(f1 , text = "submit" , command = entry).pack()
"""


#FORM and SAVING IN TXT FILE
"""
def input_fun():
    print(f"my name is {namevar.get()}")
    print(f"my father name is {fathervar.get()}")
    print(f"my mother name is {mothervar.get()}")

    with open("Record.txt" , "a") as p:
        p.write(f"My name is{namevar.get()} \nfather name is {fathervar.get()} \nmther name is 12pass {passing_var.get()}")

namevar = StringVar()
fathervar = StringVar()
mothervar = StringVar()
passing_var = IntVar()

r.geometry("500x500")
l1 = Label(r , text = "Welcome TO Poartal" , font = ("comicsansm" , 16 , "bold"))
name_label = Label(r , text = "NAME:" ).grid(row = 1 , column = 0 , padx =20)
father_label = Label(r , text = "FATHER:" ).grid(row = 2 , column = 0 , padx =20)
mother_label = Label(r , text = "MOTHER:" ).grid(row = 3 , column = 0 , padx =20)

name_entry = Entry(r , textvariable=  namevar).grid(row = 1 , column = 1)
father_entry = Entry(r , textvariable=  fathervar).grid(row = 2 , column = 1)
mother_entry = Entry(r , textvariable=  mothervar).grid(row = 3 , column = 1)
pass_button = Checkbutton(text = "Class 12 Pass" , variable = passing_var).grid(row = 4 , column = 1)
Button(r ,text = "SUBMIT" , command = input_fun).grid(row = 5 , column = 1)

l1.grid(row = 0 ,column  = 1 , padx = 100)
"""



"""
r.geometry("500x500")
canvas_width = 500
canvas_height = 500

#
def fun(event):
    print(f"your current location is {event.x} {event.y}")

    l2 = Label(r , text = event.x).pack()
    l3 = Label(r , text = event.y).pack()

b1 = Button(r , text  = "submit" , command = fun)
b1.pack(side = TOP )
b1.bind("<Button-1>" , fun)


f1 = Frame(r , borderwidth = 5 , relief = SUNKEN , bg = "red")
f1.pack(side = LEFT , fill = "y" )

can_widget = Canvas(r , width = canvas_width , height = canvas_height)
can_widget.pack()

#x1 , y1 , x2 , y2
can_widget.create_line(0, 250 , 500 ,250)
can_widget.create_line(0, 0 , 500 ,500)
can_widget.create_line(0, 500 , 500 , 0 )

#cordinates of top left and cordinates of bottom right
can_widget.create_rectangle( 5 ,5  , 495 , 495 )
"""


#window resizer program
"""
def fun():
    r.geometry(f"{x_value.get()}x{y_value.get()}")

x_value = StringVar()
y_value = StringVar()

e1 = Entry(r  , textvariable = x_value).pack()
e2 = Entry(r  , textvariable = y_value).pack()

b1 = Button(r , text = "SUBMIT" , command = fun).pack()
"""

#MENU
"""
r.geometry("500x500")
r.title("Menu")
def  fun():
    print("hello")

#menus = Menu(r)
#menus.add_command( label = "FILE" , command = fun)
#menus.add_command( label = "QUIT" , command = quit)
#r.config(menu = menus )


#DROPDOWN MENU AND SEAPARATOR
menubar = Menu(r)
m1 = Menu(menubar , tearoff = 0)

m1.add_command(label = "NEW" , command =fun)
m1.add_command(label = "SAVE" , command =fun)
m1.add_separator()
m1.add_command(label = "FIND" , command =fun)

menubar.add_cascade(label = "MENU" , menu = m1)
r.config(menu = menubar)
"""


#SLIDER
"""
r.geometry("500x500")
r.title("SLIDER")


def rupee():
    tmsg.showinfo("AMOUNT" , f"congrates you get {my_slider2.get()}")
    with open("Record.txt" , "a") as p:
        p.write(f"RATE : {my_slider2.get()}\n")

l1 = Label(r , text = "how many rippes do you want:")
my_slider1 = Scale(r  , from_ = 0 , to = 100)
my_slider1.pack()

my_slider2 = Scale(r , from_ = 0 , to = 100 , orient= HORIZONTAL , tickinterval = 25)
my_slider2.set(50)
my_slider2.pack()

b1 = Button(r , text = "Get rupee" , command = rupee).pack()
"""

#RADIO BUTTON
"""
r.geometry("500x500")
r.title("RADIO BUTTON")

def fun():
    tmsg.showinfo("ORDER" , f"Your order is {var.get()}")
var = StringVar()
var.set("hello") # Fake default selected item
l1  = Label(r , text = "What Would You Like To Have Sir/Maam" , font = ("lucida" , 15 , "bold")).pack(side = TOP)
radio  = Radiobutton(r , text = "Dosa" , variable = var , value = "Dosa").pack()
radio  = Radiobutton(r , text = "Samosa" , variable = var , value = "Samosa").pack()
radio  = Radiobutton(r , text = "Momos" , variable = var , value = "Momos").pack()
radio  = Radiobutton(r , text = "Chawmin" , variable = var , value = "Chawmin").pack()
Button(text = "ORDER NOW" , command = fun).pack()



def fun():
    tmsg.showinfo("ORDER" , f"Your order is {var2.get()}")
var2 = IntVar()
var2.set("hello") # Fake default selected item
l1  = Label(r , text = "What Would You Like To Have Sir/Maam" , font = ("lucida" , 15 , "bold")).pack(side = TOP)
radio  = Radiobutton(r , text = "Dosa" , variable = var2 , value = 1).pack()
radio  = Radiobutton(r , text = "Samosa" , variable = var2 , value = 2).pack()
radio  = Radiobutton(r , text = "Momos" , variable = var2 , value = 3).pack()
radio  = Radiobutton(r , text = "Chawmin" , variable = var2 , value = 4).pack()
Button(text = "ORDER NOW" , command = fun).pack()
"""


#LISTBOX
"""
r.geometry("500x500")
r.title("CHECKBOX")

def add_fun():
    global i
    c1.insert( ACTIVE , f"{i}")
    i = i+1
i = 0
c1 = Listbox(r)
c1.pack()
c1.insert(END , "Hello World")
b1 = Button(r , text = "ADD" , command = add_fun).pack()
"""



#SCROLLBAR
"""
r.geometry("500x500")
r.title("SCROLLBAR")

#SCROLL WITH TEXT WIDGET

scroll  = Scrollbar(r)
scroll.pack(fill = "y" , side = RIGHT )
t = Text(r , yscrollcommand = scroll.set)
t.pack(fill = "both")
scroll.config(command = t.yview)
"""



#SCROLL WITH LISTBOX
"""
def add_fun():
    for i in range(0 , 100):
        listbox.insert(END , f"{i}")


scroll2 = Scrollbar(r)
scroll2.pack(side = RIGHT , fill = "y")

listbox = Listbox(r , yscrollcommand = scroll2.set)
listbox.pack(fill = "y" , side = RIGHT ,)
listbox.insert(END , "hello" ,)
scroll2.config(command = listbox.yview)

Button(text = "Add" , command = add_fun).pack(side = RIGHT)
"""

#STATUSBAR
"""
r.geometry("500x500")
r.title("STATUS BAR")

def submit_fun():
    my_statusbar.set("busy!")
    import time
    time.sleep(2)
    my_statusbar.set("START")

my_statusbar = StringVar()
my_statusbar.set("Ready") #SET VALUE IN STRING VARIABLE
sbar = Label(r , textvariable = my_statusbar, anchor = "w" ,relief = SUNKEN ).pack(side = BOTTOM  , fill = X )
Button(r , text = "SUBMIT" , command = submit_fun).pack()
"""


#SET BACKGROUND
"""
r.config(background = "grey")
r.config(background = "black")

width = r.winfo_screenmmwidth()
height = r.winfo_screenmmheight()

print(f"{width}x{height}")
"""



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#TKK BUTTON
"""
from tkinter.ttk import *

r.geometry("400x400")
r.title("ttk Button")

Button(r ,text = "submit" , command = r.destroy).pack()


"""


r.mainloop()

