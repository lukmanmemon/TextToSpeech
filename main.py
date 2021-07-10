from tkinter import Tk, Text, Entry, Button, ttk, messagebox, filedialog, INSERT, LabelFrame
import os
import playsound
# Import module for text to speech conversion
from gtts import gTTS

gui = Tk()
width = gui.winfo_screenwidth()
height = gui.winfo_screenheight()

gui.geometry("%dx%d" % (width, height))
gui.title("Text To Speech")

text_box = Text(gui, height = 20, width = 80, undo = True, autoseparators = True, maxundo = -1)
text_box.pack(pady = 10)

def retrieve_input():
    input = text_box.get("1.0", "end")
    return input

def clear_input():
    text_box.delete("1.0", "end")

def process_input():
    if text_box.get("1.0", "end") == "\n":
        messagebox.showinfo("Error", "Please enter some text")
    else:
        language = 'en'
        myobj = gTTS(text=retrieve_input(), lang=language, slow=False)
        myobj.save("speech.mp3")   
        playsound.playsound("speech.mp3")
        os.remove("speech.mp3")

read_button = Button(gui, text = "Read text", width = 15, height = 2, bg = "#f1bb5b", command = process_input)
read_button.place(x = width * 0.47, y = height * 0.4)

def upload_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Plain text", ".txt"),))
    file = open(filename, "r")
    contents = file.read()
    file.close()

    if text_box.get("1.0", "end") != "\n":
        clear_input()

    text_box.insert(INSERT, contents)

add_file = Button(gui, text = "Upload file", width = 15, height = 2, command = upload_file)
add_file.place(x = width * 0.37, y = height * 0.4)

clear_button = Button(gui, text = "Clear", width = 15, height = 2, bg = "#f15b6c", command = clear_input)
clear_button.place(x = width * 0.57, y = height * 0.4)

def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        gui.destroy()

gui.protocol("WM_DELETE_WINDOW", on_closing)
gui.mainloop()