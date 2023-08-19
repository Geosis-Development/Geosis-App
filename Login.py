from tkinter import *
import mysql.connector
from tkinter import messagebox

color = "#36393e"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="geosis")
cursor = mydb.cursor()
 
win = Tk()
win.title("Geosis - Login")
win.geometry("800x500")
win.resizable(False,False)
win.config(bg=color)

icon = PhotoImage(file='geosis.png')
win.iconphoto(False, icon)

def submit():
    a = user.get()
    b = pas.get()
    
    x = cursor.execute(f"SELECT * FROM data WHERE (Name = '{a}' OR Email = '{a}') AND Password = '{b}'")
    result = cursor.fetchone()
    
    if result:
        win.destroy()
        import Geosis
        
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

 
def gap(j):
    for i in range(j):
        Label(win,bg=color).pack()
 
gap(2)
Label(win, text="LOGIN", font=("Consolas", 25, 'bold'), bg=color, fg="White").pack()

gap(1)
Label(win, text="Username / Email", bg=color, fg="White").pack()
user = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT)
user.pack()

gap(1)
Label(win, text="Password", bg=color, fg="White").pack()
pas = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT, show="•")
pas.pack()

def on_enter(e):
    submit['bg'] = '#cfcfcf'

def on_leave(e):
    submit['bg'] = 'White'
    
gap(1)
submit = Button(win, text="SUBMIT", font=("Consolas", 10, 'bold'), bg="white", fg="black",
                relief=FLAT, width=10, command=submit,activebackground='White')
submit.pack()

submit.bind("<Enter>", on_enter)
submit.bind("<Leave>", on_leave)

def register():
    win.destroy()
    import Register
    
def on_enter(e):
    reg['foreground'] = '#0092ff'

def on_leave(e):
    reg['foreground'] = 'White'
    
gap(1)
reg = Button(win,text="Don't Have An Account?",bg=color,fg="White",relief=FLAT
             ,activebackground=color,activeforeground="White",borderwidth=0,command=register)
reg.pack()

reg.bind("<Enter>", on_enter)
reg.bind("<Leave>", on_leave)
 
win.mainloop()
