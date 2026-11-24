from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("Interest Calculator App")

principal_label = Label(window, text="Principal amount")
principal_label.pack(pady=(20, 5))
principal_entry = Entry(window)
principal_entry.pack()

rate_label = Label(window, text="Interest rate (%)")
rate_label.pack(pady=(10, 5))
rate_entry = Entry(window)
rate_entry.pack()

years_label = Label(window, text="Time (years)")
years_label.pack(pady=(10, 5))
years_entry = Entry(window)
years_entry.pack()

result_label = Label(window, text="")
result_label.pack(pady=20)

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        years = float(years_entry.get())
        if principal < 0 or rate < 0 or years < 0:
            raise ValueError
        interest = (principal * rate * years) / 100
        total = principal + interest
        result_label.config(text=f"Interest: {interest:.2f}\nTotal amount: {total:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid non-negative numbers.")
calculate_button = Button(window,text="Calculate",bg="blue",fg="azure",command=calculate_interest,)
calculate_button.pack(pady=10)
window.mainloop()