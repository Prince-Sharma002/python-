from pytube import YouTube

link = "https://www.youtube.com/watch?v=TSUbPk6i13I"

y1 = YouTube(link)

#print(y1.title)
#print(y1.thumbnail_url)

print("To download video press 1 \nTo download audio press 2")
n = int(input("eneter choice:"))

if n == 1:
    videos = y1.streams.all()
    v = list(enumerate(videos))
    for i in v:
        print(i)

    print()
    strm = int(input(("enter in which mode you have to download video:")))

    videos[strm].download()


else:
    music = y1.streams.filter(only_audio=True)
    m = list(enumerate(music))
    for i in m:
        print(i)

    print()
    i = int(input("Enter your choice:"))

    music[i].download()
    print("your audio successfuly download")



"""
from tkinter import *
from pytube import YouTube

root = Tk()

def download():

    y1 = YouTube(link_enter.get())
    music = y1.streams.filter(only_audio=True)
    music[2].download()



#root.resizable(0, 0) # makes the window adjustable with its features
root.title('youtube downloader')

Label(root, text="Download Youtube videos for free", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=400, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=300, y=85)

bu = Button(root , text="Download" , font= "san-sarif 13  bold" , bg = "red" ,padx =2 , command="download").place(x=450 , y=130)


root.mainloop()


#In the case of textvariable , which is mostly used with Entry and Label widgets, it is a variable that will be displayed as text. When the variable changes, the text of the widget changes as well.

"""