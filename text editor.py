#text editor

from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
import os.path
from tkinter import messagebox

#------------functions------------

def change_color():
    color = colorchooser.askcolor(title="pick a color")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)

def open_file():
    file = askopenfilename(defaultextension=".txt",file=[("All Files","*.*"),("Text Documents","*.txt")])
    window.title(os.path.basename(file))
    text_area.delete(1.0,END)
    file = open(file,"r")
    text_area.insert(1.0,file.read())
  
def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all files","*.*"),
                                                                                                     ("text documents",".txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,"w")
            file.write(text_area.get(1.0,END))
        except Exception:
            print("file can not be read")
        finally:
            file.close()
def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("about this program","created by Jhon sebastian rios")

def quit():
    quit = messagebox.askyesnocancel(title="Warning",message="do you want to save changes?")
    if (quit == TRUE):
        save_file()
    elif (quit == FALSE):
        window.destroy()
    else:
        return
    

#------------initial configurations------------

window = Tk()

window.title("text editor program")
file = None

Wwidth = 500
Wheight = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

xaxis = int((screen_width/2) - (Wwidth/2))
yaxis = int((screen_height/2) - (Wheight/2))

window.geometry("{}x{}+{}+{}".format(Wwidth,Wheight,xaxis,yaxis))



font_name = StringVar(window)
font_name.set("arial")

font_size = StringVar(window)
font_size.set("25")



text_area = Text(window,font=(font_name.get(),font_size.get()))
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky= N+E+S+W)



scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)



frame = Frame(window)
frame.grid()


#------------buttons and menus------------

#--fontconfig--

color_button = Button(frame, text="color",command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1,to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

#--menubar--

menu_bar = Menu(window)
window.config(menu=menu_bar)

File_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file",menu=File_menu)
File_menu.add_command(label="new", command=new_file)
File_menu.add_command(label="open", command=open_file)
File_menu.add_command(label="save", command=save_file)
File_menu.add_separator()
File_menu.add_command(label="quit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="edit", menu=edit_menu)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy)
edit_menu.add_command(label="paste",command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="help",menu=help_menu)
help_menu.add_command(label="about",command=about)

#------------finals------------

window.mainloop()






