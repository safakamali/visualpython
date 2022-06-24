from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from os import system

window = Tk()
window.title("Visual Python")


# window.resizable(False, False)
def savefile():
    try:
        File = fd.asksaveasfile(mode='w', defaultextension=".py")
        if File:
            File.write(text.get("1.0", "end-1c"))
            File.close()
    except:
        messagebox.showerror("Error", "Not defined")


fileaddr = None


def openfile():
    global fileaddr
    fileaddr = fd.askopenfilename()
    File = open(fileaddr)
    try:
        data = File.read()
        File.close()
        text.delete("1.0", "end-1c")
        text.insert(INSERT, data)
    except:
        messagebox.showerror("Error", "This file is not supported. Only text files are supported by Programer E.")


def insert_label():
    text.insert(END, '\nLabel(root, text="Hello World")')


def insert_button():
    text.insert(END, '\nButton(root, text="Hello World", command=lambda : print("Clicked Button"))')


def insert_textbox():
    text.insert(END, '\nEntry(root)')

def insert_listbox():
    text.insert(END, "\nListbox(root)")

def new_window():
    text.insert(END, "from tkinter import *\nroot = Tk()\n\nroot.mainloop()")


def insert_set_title():
    text.insert(END, '\nroot.title("Tkinter - Visual Python")')

def run_python_script():
    File = open("tempscript.py", "w")
    File.write(text.get("1.0", "end-1c"))
    File.close()
    system(f"python tempscript.py")


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Settings", command=lambda: system("settings.txt"))
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

widget = Menu(menubar, tearoff=0)
widget.add_command(label="Window", command=new_window)
widget.add_separator()
widget.add_command(label="Title", command=insert_set_title)
widget.add_separator()
widget.add_command(label="Label", command=insert_label)
widget.add_command(label="Button", command=insert_button)
widget.add_command(label="Text Box", command=insert_textbox)
widget.add_command(label="List Box", command=insert_listbox)
menubar.add_cascade(label="Tkinter", menu=widget)

run = Menu(menubar, tearoff=0)
run.add_command(label="Run Python Script", command=run_python_script)
menubar.add_cascade(label="Run", menu=run)

settingfile = open("settings.txt")

settingsread = settingfile.read()

settingfile.close()

settings = {}

settingsline = settingsread.split("\n")

for item in settingsline:
    key_value = item.split("=")

    settings[key_value[0]] = key_value[1]

window.config(menu=menubar)
data_text = StringVar()
text = Text(window, font=(settings["font"], 13), width=150, height=38)
text.pack()

window.mainloop()
