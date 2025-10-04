from tkinter import *
from tkinter import messagebox
import os
import json
root=Tk()
root.title("ATM")
root.geometry("670x300")
root.resizable(0,0)





login=Toplevel()
login.title("Insert Cart")
login.resizable(0,0)
login.geometry("420x130")

lbl_cart=Label(login,text="Cart Number:",bg="#3C467B",fg="white",font=("Times",18,"bold"),width=12)
lbl_password=Label(login,text="Password:",bg="#3C467B",fg="white",font=("Times",18,"bold"),width=12)
ent_cart=Entry(login,fg="#50589C",font=("Times",18))
ent_password=Entry(login,fg="#50589C",font=("Times",18))
btn_cancel=Button(login,text="Cancel",fg="white",bg="#FDAAAA",font=("Times",15),width=15,command=root.destroy)
btn_login=Button(login,text="Login",fg="white",bg="#3C467B",font=("Times",15),width=21)


#login page grid
lbl_cart.grid(row=0,column=0)
lbl_password.grid(row=1,column=0)
ent_cart.grid(row=0,column=1)
ent_password.grid(row=1,column=1)
btn_cancel.grid(row=2,column=0)
btn_login.grid(row=2,column=1)

root.withdraw()
login.mainloop()
