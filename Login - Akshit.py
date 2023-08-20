#Touch mat kr thoda karke choda hu, class jana he
import mysql.connector
from tkinter import *
from tkinter import messagebox
import bcrypt
import re


def valid_ep(emailorpass):
    cursor.execute("SELECT * FROM data WHERE `Email`=%s OR `Phone_No`=%s OR `Name` =%s", (a))
    existing_user = cursor.fetchone()
        

color = "#36393F"

win = Tk()
win.title("Geosis - Login")
win.geometry("800x500")
win.config(bg=color)

#icon = PhotoImage(file='geosis.png')
#win.iconphoto(False, icon)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="geosis")
cursor = mydb.cursor()

def gap(j):
    for i in range(j):
        Label(win, text=" ", bg=color).pack()
        
def submit():
    a = ep.get()
    b = pas.get()

    if not (a and b):
        messagebox.showerror("Error", "Please Fill All The Fields.")
        return
    
    if not valid_ep(a):
        messagebox.showerror("Error", "This Email Or Phone Number is not registered")
        return
    
if existing_user:
    messagebox.showinfo("Successful", "Successfully Logged In")


gap(1)
Label(win, text="Name", bg=color, fg="White").pack()
name = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT)
name.pack()

gap(1)
Label(win, text="Password", bg=color, fg="White").pack()
pas = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT, show="•")
pas.pack()

def on_enter(e):
    log['foreground'] = '#0092ff'

def on_leave(e):
    log['foreground'] = 'White'

def register():
    win.destroy
    import register
gap(1)
log = Button(win,text="Don't Have An Account?",bg=color,fg="White",relief=FLAT
             ,activebackground=color,activeforeground="White",borderwidth=0,command=login)
log.pack()

log.bind("<Enter>", on_enter)
log.bind("<Leave>", on_leave)

win.mainloop()
