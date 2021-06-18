#3rd Way
#Import the required libraries
from tkinter import *
import webbrowser

win = Tk()

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="Click to se the New File")
link.pack()
link.bind("<Button-1>", lambda e:callback("https://drive.google.com/file/d/1-15pEvcqcn0kDPmyhiloPJdxpp735hcQ/view?usp=sharing"))

win.mainloop()