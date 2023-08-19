import mysql.connector
from tkinter import *
from tkinter import messagebox

color = "#36393F" 

win = Tk()
win.title("Geosis - Register")
win.geometry("800x500")
win.config(bg=color)

icon = PhotoImage(file = 'geosis.png')
win.iconphoto(False, icon)

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
    database = "geosis")
cursor = mydb.cursor()

def gap(j):
    for i in range(j):
        Label(win,text=" ",bg=color).pack()

def submit():
    a = name.get()
    b = email.get()
    c = phone.get()
    d = pas.get()
    
    if a or b or c or d == "":
        messagebox.showerror("Error","Please Ensure To Fill All The Fields")
    else:    
        cursor.execute(f"INSERT INTO data (`Name`, `Email`, `Phone_No`, `Password`) VALUES ('{a}','{b}','{c}','{d}')")
        mydb.commit()
        messagebox.showinfo("Successful","Successfully Registered")
gap(2)
Label(win,text="REGISTER",font=("Consolas",25,'bold'),bg=color,fg="White").pack()
    
gap(1)
Label(win,text="Name",bg=color,fg="White").pack()
name = Entry(win,bg="White",fg="gray",font=("Consolas",12),width=20,relief=FLAT)
name.pack()
gap(1)
Label(win,text="Email",bg=color,fg="White").pack()
email = Entry(win,bg="White",fg="gray",font=("Consolas",12),width=20,relief=FLAT)
email.pack()
gap(1)
Label(win,text="Phone No",bg=color,fg="White").pack()
phone = Entry(win,bg="White",fg="gray",font=("Consolas",12),width=20,relief=FLAT)
phone.pack()
gap(1)
Label(win,text="Password",bg=color,fg="White").pack()
pas = Entry(win,bg="White",fg="gray",font=("Consolas",12),width=20,relief=FLAT)
pas.pack()

gap(1)
Submit = Button(win,text="SUBMIT",font=("Consolas",10,'bold'),bg="white",fg="black",
       relief= FLAT,width=10,command=submit)
Submit.pack()

win.mainloop()