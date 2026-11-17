from datetime import date
from tkinter import Button, Entry, Label, Tk


window = Tk()
window.title("Age Calculator")
window.geometry("400x300")
window.resizable(False, False)


def calculate_age():
    name = name_entry.get().strip()
    try:
        month = int(month_entry.get())
        day = int(day_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
    except ValueError:
        result_label.config(text="Please enter a valid date of birth.")
        return

    today = date.today()
    if birth_date > today:
        result_label.config(text="Birth date cannot be in the future.")
        return

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    display_name = f"{name}, " if name else ""
    result_label.config(text=f"{display_name}you are {age} years old.")


Label(window, text="Name", width=15).grid(row=0, column=0, padx=10, pady=8)
name_entry = Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=8)

Label(window, text="Month of birth", width=15).grid(row=1, column=0, padx=10, pady=8)
month_entry = Entry(window, width=25)
month_entry.grid(row=1, column=1, padx=10, pady=8)

Label(window, text="Day of birth", width=15).grid(row=2, column=0, padx=10, pady=8)
day_entry = Entry(window, width=25)
day_entry.grid(row=2, column=1, padx=10, pady=8)

Label(window, text="Year of birth", width=15).grid(row=3, column=0, padx=10, pady=8)
year_entry = Entry(window, width=25)
year_entry.grid(row=3, column=1, padx=10, pady=8)

Button(
    window,
    text="Calculate Age",
    command=calculate_age,
    bg="darkblue",
    fg="lightblue",
).grid(row=4, column=0, columnspan=2, pady=15)

result_label = Label(window, text="", wraplength=360)
result_label.grid(row=5, column=0, columnspan=2, padx=10)

window.mainloop()