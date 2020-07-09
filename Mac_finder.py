from tkinter import Tk, Label, Button, Entry, END, messagebox as msgbx
from getmac import get_mac_address
import pyperclip

root = Tk()
root.geometry("800x400")
root.title("MAC Finder")
root.configure(bg="grey")

l1 = Label(root, text="Welcome to Mac Finder", bg="grey", font=("Times", 35, "bold underline"))
l1.pack()



def getmac():
    mac_add = get_mac_address()
    e1.delete(0, END)
    e1.insert(END, mac_add)

b1 = Button(root, text="Get Mac Address!", bg="grey", bd=10, font=("Times", 15, "bold underline"), command=getmac)
b1.place(x=310, y=100)

e1 = Entry(root, bd=10, font=("Times", 35, "bold"))
e1.place(x=200, y=200, height=80, width=390)



def copytoclip():
    pyperclip.copy(e1.get())
    msgbx.showinfo("Copied", "Your Mac Address has been copied to Clipboard")


b1 = Button(root, text="Copy To Clipboard", bg="grey", bd=10, font=("Times", 15, "bold"), command=copytoclip)
b1.place(x=310, y=280)

my_label = Label(root, text="Program@Paras4902", bg="grey", font=("helvetica", 15, "italic"))
my_label.place(x=600, y=370)
root.mainloop()
