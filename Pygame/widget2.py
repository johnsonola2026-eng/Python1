from tkinter import *
from datetime import date

window=Tk()
window.title('getting started with widgets')
window.geometry('400x300')
window.mainloop()

lbl=Label(text="Hey there!",fg="white",bg="black",height=1,width=300)
name_lbl=Label(text="full name",bg="lightgray")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message
    message="welcome to the application! \n Today's date is:"
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="begin", command=display, height=1, bg="lightblue", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()