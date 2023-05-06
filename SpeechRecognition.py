                                                # Sofia

import pyaudio
import speech_recognition as sr
import re

import openai
openai.api_key = "YOUR_API_KEY"

import pyttsx3

# initialize the engine
engine = pyttsx3.init()
# set the rate of speech
engine.setProperty('rate', 130)
# set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change index to change voice

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen( source , phrase_time_limit=10 )

    try:
        print("Recognizing...")
        command = r.recognize_google( audio , language="en-in")
        print(f"You Said:{command}")
    except Exception as e:
        return "none"

    return command    

while True:
    command = takecommand().lower()

    if( ("sofia" in command) ):
        command = command.replace("sofia" , "")

        print("searched item:" ,command)        
        completion = openai.Completion.create(
        engine = "text-davinci-003",    
        prompt = command ,
        max_tokens = 1000
        )        
        speak( completion.choices[0]["text"] )
