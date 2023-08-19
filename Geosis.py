from tkinter import *
import Login

color = "#36393e"

win = Tk()
win.title("Geosis - Homepage")
win.geometry("800x500")
win.resizable(False,False)
win.config(bg=color)

icon = PhotoImage(file='geosis.png')
win.iconphoto(False, icon)



win.mainloop()
