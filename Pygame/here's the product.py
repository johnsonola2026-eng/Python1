from tkinter import *
window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

Label(window, text="Enter the first number:", fg="darkblue", bg="lightblue").pack(fill="x", padx=10, pady=(20, 5))
first_entry = Entry(window)
first_entry.pack(padx=10, pady=5)
Label(window, text="Enter the second number:", fg="darkblue", bg="lightblue").pack(fill="x", padx=10, pady=5)
second_entry = Entry(window)
second_entry.pack(padx=10, pady=5)
result_label = Label(window, text="Product:")
result_label.pack(pady=10)

def calculate_product():
    try:
        first_value = float(first_entry.get())
        second_value = float(second_entry.get())
        product = first_value * second_value
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    result_label.config(text=f"Product: {product:g}")
Button(window, text="Calculate", command=calculate_product).pack(pady=5)
window.mainloop()