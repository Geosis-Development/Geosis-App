import mysql.connector
from tkinter import *
from tkinter import messagebox
import bcrypt
import re

color = "#36393F"

win = Tk()
win.title("Geosis - Register")
win.geometry("800x500")
win.config(bg=color)

icon = PhotoImage(file='geosis.png')
win.iconphoto(False, icon)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="geosis")
cursor = mydb.cursor()

def gap(j):
    for i in range(j):
        Label(win, text=" ", bg=color).pack()

def valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(email_pattern, email)

def valid_phone(phone):
    phone_pattern = r'^\d{10}$'
    return re.match(phone_pattern, phone)

def valid_name(name):
    name_pattern = r'^[a-zA-Z]+$'
    return re.match(name_pattern, name)

def submit():
    a = name.get()
    b = email.get()
    c = phone.get()
    d = pas.get()

    if not (a and b and c and d):
        messagebox.showerror("Error", "Please Fill All The Fields.")
        return
    
    if not valid_name(a):
        messagebox.showerror("Error", "Please Enter A Valid Name With Only Alphabetic Characters.")
        return
    
    if not valid_email(b):
        messagebox.showerror("Error", "Please Enter A Valid Email Address.")
        return

    if not valid_phone(c):
        messagebox.showerror("Error", "Please Enter A Valid 10-Digit Phone Number.")
        return

    hashed_password = bcrypt.hashpw(d.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("SELECT * FROM data WHERE `Email`=%s OR `Phone_No`=%s", (b, c))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "User Already Registered With This Email Or Phone Number.")
        else:
            cursor.execute("INSERT INTO data (`Name`, `Email`, `Phone_No`, `Password`) VALUES (%s, %s, %s, %s)",
                           (a, b, c, hashed_password))
            mydb.commit()
            messagebox.showinfo("Successful", "Successfully Registered")
            clear_entries()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        messagebox.showerror("Error", "An Error Occurred While Registering.")

def clear_entries():
    name.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    pas.delete(0, END)

gap(2)
Label(win, text="REGISTER", font=("Consolas", 25, 'bold'), bg=color, fg="White").pack()

gap(1)
Label(win, text="Name", bg=color, fg="White").pack()
name = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT)
name.pack()

gap(1)
Label(win, text="Email", bg=color, fg="White").pack()
email = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT)
email.pack()

gap(1)
Label(win, text="Phone No", bg=color, fg="White").pack()
phone = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT)
phone.pack()

gap(1)
Label(win, text="Password", bg=color, fg="White").pack()
pas = Entry(win, bg="White", fg="gray", font=("Consolas", 12), width=20, relief=FLAT, show="•")
pas.pack()

gap(1)
Submit = Button(win, text="SUBMIT", font=("Consolas", 10, 'bold'), bg="white", fg="black",
                relief=FLAT, width=10, command=submit,activebackground='White')
Submit.pack()

def login():
    win.destroy()
    import Login
    
def on_enter(e):
    log['foreground'] = '#0092ff'

def on_leave(e):
    log['foreground'] = 'White'
    
gap(1)
log = Button(win,text="Already Have An Account?",bg=color,fg="White",relief=FLAT
             ,activebackground=color,activeforeground="White",borderwidth=0,command=login)
log.pack()

log.bind("<Enter>", on_enter)
log.bind("<Leave>", on_leave)

win.mainloop()
