from tkinter import Tk, Text, Entry, Button, ttk, messagebox, filedialog, INSERT
import playsound
# Import module for text to speech conversion
from gtts import gTTS

gui = Tk()
gui.geometry("750x500")
gui.title("Text to speech")

text_box = Text(gui, height = 20, width = 80)
text_box.pack(pady = 10)

def retrieve_input():
    input = text_box.get("1.0", "end")
    return input

def empty_input():    
    if text_box.get("1.0", "end") == "\n":
        messagebox.showinfo("Error", "Please enter some text")
    else:
        gui.quit()

read_button = Button(gui, text = "Read", width = 10, bg = "orange", command = empty_input)
read_button.place(x = 300, y = 250)
read_button.pack(pady = 10)

def import_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Plain text", "*.txt"),))
    txt_file = open(filename, "r")
    contents = txt_file.read()
    txt_file.close()
    text_box.insert(INSERT, contents)
    return contents

add_file = Button(gui, text = "Import file", width = 10, command = import_file)
add_file.place(x=400, y=250)
add_file.pack()

def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        gui.destroy()

gui.protocol("WM_DELETE_WINDOW", on_closing)
gui.mainloop()

mytext = retrieve_input()
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("speech.mp3")

playsound.playsound("speech.mp3")