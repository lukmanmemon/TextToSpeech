from tkinter import Tk, Text, Entry, Button

# Import module for text to speech conversion
from gtts import gTTS
# Module to play converted audio
import os

gui = Tk()
gui.geometry("750x300")

text_box = Text(gui, height = 15, width = 60)
text_box.pack()

def retrieve_input():
    input = text_box.get("1.0", "end-1c") # This is the text you may want to use later
    return input

b = Button(gui, text = "OK", width = 10, command = gui.quit)
b.pack()

gui.mainloop()

mytext = retrieve_input()
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("test.mp3")
# Playing converted file 
os.system("start test.mp3")
