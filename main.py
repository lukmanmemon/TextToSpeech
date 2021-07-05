from tkinter import Tk, Text, Entry, Button, ttk, messagebox, filedialog, INSERT
import playsound
# Import module for text to speech conversion
from gtts import gTTS


gui = Tk()
gui.geometry("750x300")
gui.title("Text to speech")

text_box = Text(gui, height = 15, width = 60)
text_box.pack()

def retrieve_input():
    input = text_box.get("1.0", "end")
    return input

read_button = Button(gui, text = "Read", width = 10, bg = "orange", command = gui.quit)
read_button.pack()

def import_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = ([("text files", ".txt"), ("DOCX", ".docx")]))
    txt_file = open(filename, "r")
    contents = txt_file.read()
    txt_file.close()
    text_box.insert(INSERT, contents)
    return contents

add_file = Button(gui, text = "Import file", width = 10, command = import_file)
add_file.pack()

gui.mainloop()

mytext = retrieve_input()
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("text.mp3")

playsound.playsound("text.mp3")