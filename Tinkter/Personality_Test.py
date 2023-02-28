import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk , Image


r = Tk()
r.config(cursor = "plus")

r.title("Personality Test")
r.geometry("1000x1000")
menu_frame = Frame(r)
menu2_Frame = Frame(r)
foot_frame =Frame(r)
greek_frame = Frame(r)
roman_Frame = Frame(r)
sqaure_frame = Frame(r)



def change_to_menu2():
    menu_frame.forget()
    menu2_Frame.pack(fill = "both" , expand = 1)

def change_to_menu():
    menu2_Frame.forget()

    menu_frame.pack(fill = "both" , expand = 1)

def change_to_menu3():
    foot_frame.forget()
    greek_frame.forget()
    roman_Frame.forget()
    sqaure_frame.forget()
    menu2_Frame.pack(fill="both", expand=1)


def change_to_foot():
    menu2_Frame.forget()
    foot_frame.pack(fill = "both" , expand= 1)

def change_to_greek():
    menu2_Frame.forget()
    greek_frame.pack(fill = "both" , expand= 1)

def change_to_roman():
    menu2_Frame.forget()
    roman_Frame.pack(fill = "both" , expand= 1)

def change_to_square():
    menu2_Frame.forget()
    sqaure_frame.pack(fill = "both" , expand= 1)

#MENU FRAME
menu_frame.pack(fill = "both" , expand = 1 )
l1 = Label(menu_frame, text = "PERSONALITY TEST" , font = ("lucida" , 40 ,"bold")).pack(ipady = 300)
b1 = Button(menu_frame , text = "NEXT" , command = change_to_menu2).pack()


#FOOT FRAME
l2 = Label(menu2_Frame , text = "FOOT SHAPE PERSONALITY TEST" , font = ("comicsansm" , 30 , "bold" )).pack(pady = 40)
b2 = Button(menu2_Frame , text = "BACK" , command = change_to_menu).pack(side = BOTTOM , pady = 50)

egypt_i = Image.open("egyptian-foot-shape-personality-traits.png")
im_1 = egypt_i.resize((150, 150))
img_1  = ImageTk.PhotoImage(im_1)
egypt_b = Button(menu2_Frame , image =img_1 , command = change_to_foot).pack(side =LEFT , padx = 50)

roman_i = Image.open("roman-foot-shape-personality-traits.png")
im_3 = roman_i.resize((150 , 150))
img_3 = ImageTk.PhotoImage(im_3)
roman_b = Button(menu2_Frame , image =img_3 , command  = change_to_roman).pack(side = LEFT, padx = 50)

greek_i = Image.open("greek-foot-shape-personality-trait.png")
im_2 = greek_i.resize((150 , 150))
img_2 = ImageTk.PhotoImage(im_2)
greek_b = Button(menu2_Frame , image =img_2 , command  = change_to_greek).pack(side = LEFT, padx = 50)


square_i = Image.open("square-foot-shape-personality-traits.png")
im_4 = square_i.resize((150,150))
img_4 = ImageTk.PhotoImage(im_4)
square_b = Button(menu2_Frame, image =img_4 , command  = change_to_square).pack(side = LEFT, padx = 30)


#FOOT FRAME
egypt_title = Label(foot_frame , text = "EGYPTIAN FOOT" , font = ("lucida" , 30 , "bold") ,underline = True).pack(pady = 20)

egypt_ia = Image.open("egyptian-foot-shape-personality-traits.png")
im_1a = egypt_ia.resize((150, 150))
img_1a  = ImageTk.PhotoImage(im_1a)
img_la = Label(foot_frame , image = img_1a , borderwidth = 2 , relief = SUNKEN).pack(pady = 50)


foot_label_label = \
     Label(foot_frame, text = "\n 1) You love being treated like royalty.\n\n"
     " 2) You are highly guarded and do not like to invasion in your privacy.\n\n"
     " 3) You are usually pretty friendly but quite secretive too.\n\n"
     " 4) You tend to keep their thoughts to themselves. Very few people get to know their minds.\n\n"
     " 5) People with Egyptian foot shape are usually lost in their own dream world.\n\n"  
     " 6) You can also be impulsive and rebellious.\n\n"
     " 7) They can be moody and have outbursts of energy as per their own mood.\n" ,
      borderwidth = 5 , relief = SUNKEN , font =("lucida") ).pack(pady = 20 )


b2 = Button(foot_frame , text = "BACK" , command = change_to_menu3).pack(side = BOTTOM , pady = 20)



#GREEK FRAME
greek_title = Label(greek_frame, text = "GREEK FOOT" , font = ("lucida" , 30 , "bold") ,underline = True).pack(pady = 20)

greek_ib = Image.open("greek-foot-shape-personality-trait.png")
im_2b = greek_ib.resize((150 , 150))
img_2b = ImageTk.PhotoImage(im_2b)
img_2l = Label(greek_frame , image = img_2b , borderwidth = 2 , relief = SUNKEN).pack(pady = 50)


greek_label = tkinter.ttk.Label(greek_frame , text = "\n 1)You are a creative individual who loves bringing new ideas.\n\n"
                                         " 2) You are highly enthusiastic and motivational.\n\n"
                                         " 3) You are also quite impulsive and always high on energy.\n\n"
                                         " 4) However, people with Greek foot shape are prone to taking stress.\n\n"
                                         " 5) They also struggle with decision-making.\n\n"
                                         " 6) Their high energy levels also lead to exhaustion or burnout at times.\n\n"
                                         " 7) People with Greek foot shape are also known to stick to their opinions and exhibit ‘my way or the highway’ attitude.\n\n"
                        ,borderwidth = 5 , relief = SUNKEN , font =("lucida")
                    ).pack(pady = 20)


b2 = Button(greek_frame , text = "BACK" , command = change_to_menu3).pack(side = BOTTOM , pady = 20)




#ROMAN FRAME

roman_title = Label(roman_Frame, text = "ROMAN FOOT" , font = ("lucida" , 30 , "bold") ,underline = True).pack(pady = 20)

b2 = Button(roman_Frame, text = "BACK" , command = change_to_menu3).pack(side = BOTTOM , pady = 20)

roman_ic = Image.open("roman-foot-shape-personality-traits.png")
im_3c = roman_ic.resize((150 , 150))
img_3c = ImageTk.PhotoImage(im_3c)
img_3l = Label(roman_Frame , image = img_3c , borderwidth = 2 , relief = SUNKEN).pack(pady = 50)


roman_label = Label(roman_Frame , text = "\n 1) You are charismatic, courageous, and outgoing.\n\n"
                                         " 2) You enjoy social settings where you get to meet new people, and discover new cultures.\n\n"
                                         " 3) You also make a loyal partner who loves spending time with their loved ones.\n\n"
                                         " 4) You would go the extra mile for their happiness.\n\n"
                                         " 5) People with Roman foot shape lead a well-balanced life and usually maintain a proportionate body shape.\n\n"
                                         " 6) Most travellers are found to have the roman foot shape.\n\n"
                                         " 7) However, they can also be arrogant or stubborn.\n\n"

                                    ,borderwidth = 5 , relief = SUNKEN , font =("lucida")
                                    ).pack(pady = 20)




#SQAURE FRAME

square_title = Label(sqaure_frame, text = "SQAURE FOOT" , font = ("lucida" , 30 , "bold") , underline = True).pack(pady = 20)

b2 = Button(sqaure_frame , text = "BACK" , command = change_to_menu3).pack(side = BOTTOM , pady = 20)

square_id = Image.open("square-foot-shape-personality-traits.png")
im_4d = square_id.resize((150,150))
img_4d = ImageTk.PhotoImage(im_4d)
img_4l = Label(sqaure_frame , image = img_4d , borderwidth = 2 , relief = SUNKEN).pack(pady = 50)

square_label = Label(sqaure_frame , text = "\n 1) You are practical, reliable, honest, and balanced.\n\n"
                                           " 2) You will carefully examine all details, and go through all the pros & cons of a matter before taking any decision.\n\n"
                                           " 3) Your decisions are influenced by very solid principles.\n\n"
                                           " 4) People with square foot shape are always weighing the positive and negative.\n\n"
                                           " 5) They have excellent conflict resolution quality.\n\n"
                                           " 6) They are also quite analytical. They are also very secure in themselves.\n\n"
                                           " 7) They are reliable and do not get easily influenced by outer circumstances or momentary impulses.\n\n "
                                    ,borderwidth = 5 , relief = SUNKEN , font =("lucida")
                                    ).pack(pady = 20)





r.mainloop()


