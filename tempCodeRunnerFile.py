import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#2C2C2C")

display_var = tk.StringVar()
display_var.set('0')
display = tk.Entry(root, font=("Arial", 24), justify="right", bg="#444", fg="white", bd=0)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

history = tk.Text(root, font=("Arial", 12), bg="#444", fg="#888", height=5, state="disabled")
history.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

history_text = ""

def update_display(value):
    global history_text
    if display.get() == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, value)
    history_text += value

def clear_display():
    display.delete(0, tk.END)
    display.insert(0, "0")
    global history_text
    history_text = ""

def evaluate():
    global history_text
    try:
        result = str(eval(display.get().replace("×", "*").replace("÷", "/")))
        history.configure(state="normal")
        history.insert(tk.END, f"{history_text} = {result}\n")
        history.configure(state="disabled")
        clear_display()
        update_display(result)
        history_text = ""
    except:
        clear_display()
        update_display("Error")
        history_text = ""

buttons = [
    ("(", ")", "%", "AC"),
    ("7", "8", "9", "÷"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "×"),
    ("0", ".", "=", "+"),
]

button_width = 5
button_height = 2

for i, row in enumerate(buttons):
    for j, value in enumerate(row):
        if value == "=":
            tk.Button(root, text=value, command=evaluate, font=("Arial", 16), bg="#333", fg="white", width=button_width, height=button_height).grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        elif value == "AC":
            tk.Button(root, text=value, command=clear_display, font=("Arial", 16), bg="#333", fg="white", width=button_width, height=button_height).grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        elif value in ["+", "-", "×", "÷"]:
            tk.Button(root, text=value, command=lambda x=value: update_display(x), font=("Arial", 16), bg="#333", fg="white", width=button_width, height=button_height).grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        else:
            tk.Button(root, text=value, command=lambda x=value: update_display(x), font=("Arial", 16), bg="#333", fg="white", width=button_width, height=button_height).grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

for i in range(4):
    root.grid_rowconfigure(i+1, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()