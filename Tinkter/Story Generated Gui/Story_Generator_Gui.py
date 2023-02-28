import random
from tkinter import *
from tkinter.ttk import *
from random import *

r = Tk()

r.title("STORY GENERATOR")
r.geometry("15000x15000")

#FUNCTIONS
def change_to_horror_frame():
    menu_frame.forget()
    horror_frame_menu.pack(expand = True , fill = "both")

def change_to_adventure_frame():
    menu_frame.forget()
    adventure_frame_menu.pack(expand = True , fill = "both")

def change_to_crime_frame():
    menu_frame.forget()
    crime_frame_menu.pack(expand = True , fill = "both")





#FRAMES
menu_frame = Frame(r)
menu_frame.pack()

horror_frame_menu = Frame()
adventure_frame_menu = Frame()
crime_frame_menu = Frame()



#MENU FRAME
app_title = Label(menu_frame , text = "STORY GENERATOR" ,font = ("lucida" , 50 , "bold")).pack(pady = 20)
category_label = Label(menu_frame , text = "CATEGORY" , font = ("lucida" , 20 )).pack(pady = (70, 10))

horror_button = Button(menu_frame , text = "HORROR" , command = change_to_horror_frame ).pack(pady = 30 , ipadx = 20)
adventure_button = Button(menu_frame , text = "ADVENTURE" , command = change_to_adventure_frame ).pack(pady = 30 , ipadx = 20)
crime_button = Button(menu_frame , text = "CRIME" , command = change_to_crime_frame ).pack(pady = 30 , ipadx = 20)


#ADVENTURE FRAME

def story_generate_fun():
    import random
    Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
    character = [f' there lived a king named {main_character_variable.get()}.',
                 f'there was a man named Jack {main_character_variable.get()}.',
                 ' there lived a farmer.']
    time = [' One day', ' One full-moon night']
    story_plot = [' he was passing by', ' he was going for a picnic to ']
    place = [' the mountains', ' the garden']
    second_character = [' he saw a man', ' he saw a young lady']
    age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
    work = [' searching something.', ' digging a well on roadside.']
    s = (random.choice(Sentence_starter) + random.choice(character) +
         random.choice(time) + random.choice(story_plot) +
         random.choice(place) + random.choice(second_character) +
         random.choice(age) + random.choice(work))

    l = Label(adventure_frame_menu , text = s).pack()


main_character_variable = StringVar()

main_character_label = Label(adventure_frame_menu , text = "PROTAGIONIST NAME:" , font = ("comicsansm"))\
    .pack( pady = 20)
main_character = Entry(adventure_frame_menu , textvariable = main_character_variable).pack()

# Defining list of phrases which will help to build a story



# Selecting an item from each list and concatenating them.

generate_button = Button(adventure_frame_menu , text = "GENERATE" , command = story_generate_fun).pack(side = BOTTOM , pady =20)




#HORROR FRAME

#use comicsansm

#prince - main character
#shubham - main character best friend
#aryan  - target boy
#other - manu, akash , chhavvi , suhani  , anushka , sona  , tanu

s  = "2022-02-12 " \
     "On a trip 11 young mens and womens depart from Delhi to Nanital." \
     "In starting it was delighted and entertained trip." \
     "shubham - Prince , lets have some fun with aryan" \
     "Prince - what do you think i invited him for the trip" \
     "both - giggles" \
     "" \
     "Aryan is a timid and unacceptable boy.He always want to make a friendly relationship with his friends" \
     "He always gaze at his friends enjoy together but was unable to indulge in their moments" \
     "" \
     "-Bus stop at Dhaba for the break-" \
     "All moved to dhaba except Prince and Shuham" \
     "" \
     "Prince - lets hide his bag inside our my bag and then move to Dhaba" \
     "shubham - right" \
     "" \
     "-At Dhaba-" \
     "" \
     "Prince - suhani where is Aryan?" \
     "suhani - may be he is in washroom.by the way why do you invite him in this trip?" \
     "Prince - Nothing big deal , he just wanted to enjoy with us in this trip." \
     "suhani - yeah his is enjoyig too much with us" \
     "both  - laugh slowly" \
     "" \
     "Prince - shubham , aryan is in washroom" \
     "shubham - then what" \
     "prince - fool lets lock his washroom gate from outside" \
     "shubham - ohh! yes" \
     "" \
     "Prince and Shubham move to washroom" \
     "" \
     "Shubham - Prince , this is a good opurtunity no one is there" \
     "Prince - Yes i can see" \
     "" \
     "Prince lock the door" \
     "After some time" \
     "All of them came back in the bus except aryan" \
     "The bus is ready to start , suddenly tanu say" \
     "" \
     "Tanu - hey guys aryan is not present here" \
     "sona - ohh god where is the damn boy right now , Prince go and search him" \
     "" \
     "Suddenly aryan enters" \
     "taking deep breath and in a panic situation" \
     "" \
     "sona - where you had been silly boy , you have wasted our time." \
     "" \
     "aryan , soory guys but this is not my fault , someone locked me in the washroom , i screamed too much and finally" \
     "someone came and help me" \
     "" \
     "Everbody - laugh" \
     "" \
     "Tanu - aryan take a seat" \
     "" \
     "suhani - (in low voice) Prince you locked him in the washroom , right" \
     "Prince - true" \
     "" \
     "both - giggles" \
     "" \
     "manu - Why are both of you giggling" \
     "suhani - prince is the one who prank with him" \
     "manu - (snicker) this is the reason you invite him in this trip" \
     "" \
     "prince - right boy " \
     "" \
     "manu - next time we together prank with him" \
     "" \
     "prince - sure " \
     "" \
     "The bus stop at its destination at 7:00 PM.They reached their destination at 7:30 PM" \
     "" \
     "Tanu - guys the cottage semms spooky" \
     "everybody  - yeeh" \
     "prince - aryan , are you scare" \
     "" \
     "everybody except aryan and tanu - laugh" \
     "tanu - stop it guys , lets go" \
     "" \
     "All of them enjoy till 11:30 PM keeping aryan at the corner" \
     "At 12:00 PM Prince talk about his plan with suhani , shubham , manu , akash to prank with aryan" \
     "" \
     "Prince - ( in low voice ) listen guys i managed to bring 3 ghost costumes with me" \
     "prince - suhani will ask for aryan to get water at that moment manu will cover his mouth with his hand from " \
     "his back" \
     "and me and shubham will scare him with full of our energy" \
     "alright guys" \
     "" \
     "everybody - aright" \
     "" \
     "At 12:10" \
     "suhani enetr in aryan's room" \
     "" \
     "suhani - aryan can you provide me a water bottle from fridge , i am unable to have a clear vision" \
     "" \
     "aryan - sure" \
     "" \
     "aryan move to get a water bottle" \
     "place is filled with darkness" \
     "aryan is in scare , moving with his phobia" \
     "suddenly manu cover his mouth from his back with his hand" \
     "prince and shubham pop up in front of him with thier ghost costumes and frighten him with horror activities" \
     "aryan cry and scream but his mouth is cover by manu" \
     "he is in full panic situation , try to escape but he can't" \
     "suddenly the panic situation is over" \
     "aryan dead due to cardiac arrest" \
     "" \
     "" \
     "" \
     "" \
     "" \



r.mainloop()