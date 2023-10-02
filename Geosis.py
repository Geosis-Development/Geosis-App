from tkinter import *
from tkinter import scrolledtext
import socket
import threading

color = "#313338"

win = Tk()
win.title("Geosis - Chat Aapp")
win.geometry("800x500")
win.resizable(False, False)
win.config(bg=color)

icon = PhotoImage(file='geosis.png')
win.iconphoto(False, icon)

# CANVAS
side = Canvas(win, bg="#2b2d31", width=250, borderwidth=0, highlightthickness=0)
side.pack(side=LEFT, fill=Y)

top = Canvas(win, bg="#313338", height=40,width=800, borderwidth=0,
             highlightthickness=0)
top.pack(side=TOP)

Label(win, bg=color).pack(side=TOP)
Label(win, bg=color).pack(side=BOTTOM)

MsgFrame = Frame(win, bg=color)
MsgFrame.pack(side=BOTTOM)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            MsgListBox.insert(END, message + '\n')
        except:
            print("Connection Lost")
            break

def send_message(event=None):
    message = MsgEntry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        MsgListBox.insert(END, "You: " + message + '\n')
        MsgEntry.delete(0, END)

def on_closing():
    client_socket.close()
    win.destroy()

MsgListBox = Listbox(win, width=50, height=16,font=("Consolas", 15),
                          bg=color,fg="white",relief=SOLID)
Scroll = Scrollbar(win, orient=VERTICAL, command=MsgListBox.yview)
Scroll.pack(side=RIGHT, fill=Y)
MsgListBox.config(yscrollcommand=Scroll.set)
MsgListBox.pack(side=TOP)

def clear_entry(event):
    MsgEntry.delete(0, END)
def fill_entry(event):
    a = MsgEntry.get()
    if a == "":
        MsgEntry.insert(0, " Message")
    else:
        MsgEntry.insert(0,"")
        
MsgEntry = Entry(MsgFrame, width=40, font=("Consolas", 18),bg="#383a40", 
                 fg="#b5bac1",bd=2,relief=FLAT)
MsgEntry.pack(side=LEFT)
MsgEntry.insert(0, " Message")
MsgEntry.bind('<FocusIn>', clear_entry)
MsgEntry.bind('<FocusOut>', fill_entry)
MsgEntry.bind('<Return>', lambda e: send_message())

Label(MsgFrame, bg=color).pack(side=BOTTOM)

# SEARCH
def clear_search(event):
    Se.delete(0, END)
def fill_search(event):
    a = Se.get()
    if a == "":
        Se.insert(0, " Search")
    else:
        Se.insert(0, "")

Label(win,bg = "#2b2d31",fg="White",
      text="_____________________________________________").place(x=9,y=45)
        
Se = Entry(win,font=("Consolas",15),relief=FLAT,bg="#383a40",fg="#b5bac1")
Se.place(x=12,y=17)
Se.insert(0, " 🔍 Search")
Se.bind('<FocusIn>', clear_search)
Se.bind('<FocusOut>', fill_search)

Cb = Button(win,text="AI Chatbot",bg=color,fg="White",font=("Consolas",15),
            width=20,relief=FLAT).place(x=11,y=80)

win.protocol("WM_DELETE_WINDOW", on_closing)

# SERVER CONNECTION
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.20', 8080))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

win.mainloop()
