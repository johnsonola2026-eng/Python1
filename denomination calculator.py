from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()
window.title('denomination counter')
window.geometry('650x400')
window.configure(bg='light blue')

upload=Image.open('Tally.jpg')
upload=upload.resize((300,300))
upload=ImageTk.PhotoImage(upload)
label=Label(window, image=Image, bg='light blue')
Label.place(x=180,y=20)
label1=Label(
    window,
    text='Hey user, Welcome to denomination calculator application',
    bg='light blue'
)
label1.place(relx=0.5,y=340 anchor=)