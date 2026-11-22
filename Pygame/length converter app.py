from tkinter import *
window = Tk()
window.title("Length Converter App")
window.geometry("400x300")
window.resizable(False, False)

def convert_inches():
    try:
        inches = float(inches_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    centimeters = inches * 2.54
    result_label.config(text=f"{inches:g} inches = {centimeters:g} centimeters")
Label(window, text="Inches", font=("Arial", 12)).pack(pady=(30, 5))
inches_entry = Entry(window, width=20)
inches_entry.pack()
Button(window,text="Convert to Centimeters",command=convert_inches,bg="blue",fg="white",).pack(pady=20)
result_label = Label(window, text="", font=("Arial", 12), wraplength=360)
result_label.pack(pady=10)
window.mainloop()