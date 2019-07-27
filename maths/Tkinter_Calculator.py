# calculator with some exception handling
#Learn about Tkinter library form https://docs.python.org/3/library/tkinter.html


import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")

label = tk.Label(root, text="Enter first number", pady=(10))
label.pack()

first_number_entry = tk.Entry(root)
first_number_entry.pack()

label2 = tk.Label(root, text="Enter second number")
label2.pack()

second_number_entry = tk.Entry(root)
second_number_entry.pack()

operations = tk.Label(root, text="Operations")
operations.pack()

def addition():
    first, second = takeValueInput()
    result = first + second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def subtract():
    first, second = takeValueInput()
    result = first - second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def multiply():
    first, second = takeValueInput()
    result = first * second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def divide():
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


addition_button = tk.Button(root, text="+",
                            command=lambda : addition())
addition_button.pack()

minus_button = tk.Button(root, text="-",
                         command=lambda : subtract())
minus_button.pack()

multiply_button = tk.Button(root, text="*",
                            command=lambda : multiply())
multiply_button.pack()

division_button = tk.Button(root, text="/",
                            command=lambda : divide())
division_button.pack()

result_label = tk.Label(root, text="Operations result is:")
result_label.pack()
