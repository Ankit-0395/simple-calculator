import tkinter as tk
from tkinter import messagebox


def button_click(symbol):
    global expression
    expression += str(symbol)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")
        clear()
    except:
        messagebox.showerror("Error", "Invalid input!")
        clear()


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x420")
root.configure(bg="#1c1c1c")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()


display = tk.Entry(root, textvariable=equation, font=("Helvetica", 20), bg="#000", fg="white",
                   bd=5, relief="sunken", justify="right")
display.pack(pady=15, padx=10, fill="x")


frame = tk.Frame(root, bg="#1c1c1c")
frame.pack()


buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("C", 3, 3),
]


for (text, row, col) in buttons:
    action = clear if text == "C" else lambda val=text: button_click(val)
    tk.Button(frame, text=text, font=("Arial", 16), bg="#333", fg="white",
              width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)


equal_btn = tk.Button(root, text="=", font=("Arial", 18), bg="#00b33c", fg="white",
                      height=2, command=calculate)
equal_btn.pack(fill="x", padx=10, pady=10)

root.mainloop()