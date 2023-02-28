from tkinter import *
import time
import random

p = Tk()


r = ""

l = chr(random.randint(ord("a") , ord("z")))
C = chr(random.randint(ord("A") , ord("Z")))
i  = str(random.randint(0 ,9))

l2 = [l , C , i]

def fun():


    global r
    for i in range(8):
        r = r + random.choice(l2)


    for j in r:
        if j in l2:
            continue
        else:
            fun()

    l1 = Label(p, text=r).pack()


Button( p , text = "GENERATE" , command  = fun).pack()

p.mainloop()