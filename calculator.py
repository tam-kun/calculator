from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log, radians

window = Tk()
screenSize = "700x800"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calculator")

# Function
def about():
    messagebox.showinfo('About',"Made by B233000012 Tamiraa")

def clickButton(item):
    global expression
    inputText.set(inputText.get() + str(item))

def clearButton():
    global expression
    expression = ""
    inputText.set("")

def clearAll():
    inputText.set("")

def expand():
    global screenSize
    if screenSize == "700x800":
        screenSize = "800x900"
    else:
        screenSize = "700x800"
    window.geometry(screenSize)

def toggleFullScreen(event):
    window.attributes("-fullscreen", not window.attributes("-fullscreen"))

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
        add_history(result)
    except:
        result = "ERROR..."
        inputText.set(result)

def add_history(result):
    history_label.config(text=history_label.cget("text") + "\n" + inputText.get())

def sin_function():
    try:
        result = sin(float(inputText.get()))
        inputText.set(result)
        add_history(result)
    except:
        inputText.set("ERROR")

def cos_function():
    try:
        result = cos(float(inputText.get()))
        inputText.set(result)
        add_history(result)
    except:
        inputText.set("ERROR")

def tan_function():
    try:
        result = tan(float(inputText.get()))
        inputText.set(result)
        add_history(result)
    except:
        inputText.set("ERROR")

def clear_history():
    history_label.config(text="")

# Menubar
menubar = Menu(window, bg="black", fg="white")
filemenu = Menu(menubar, tearoff=0, bg="black", fg="white")
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0, bg="black", fg="white")
editmenu.add_command(label="Clear History", command=clear_history)
menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0, bg="black", fg="white")
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50, fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack(side=LEFT)

buttons = [
    "AC", "Clear", "Expand", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "=", "(",
    ")", "pi", "e", "sin",
    "cos", "tan", "log"
]

row_num = 0
col_num = 0

for button_text in buttons:
    if button_text == "AC":
        btn = Button(mainFrame, text=button_text, fg="black", command=clearAll)
    elif button_text == "Clear":
        btn = Button(mainFrame, text=button_text, fg="black", command=clearButton)
    elif button_text == "=":
        btn = Button(mainFrame, text=button_text, fg="black", command=equalButton)
    elif button_text == "Expand":
        btn = Button(mainFrame, text=button_text, fg="black", command=expand)
    elif button_text == "sin":
        btn = Button(mainFrame, text=button_text, fg="black", command=sin_function)
    elif button_text == "cos":
        btn = Button(mainFrame, text=button_text, fg="black", command=cos_function)
    elif button_text == "tan":
        btn = Button(mainFrame, text=button_text, fg="black", command=tan_function)
    else:
        btn = Button(mainFrame, text=button_text, fg="black", command=lambda btn_text=button_text: clickButton(btn_text))
    
    btn.grid(row=row_num, column=col_num, padx=5, pady=5, ipadx=20, ipady=20)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

window.bind("<F11>", toggleFullScreen)

# Section to display the last 4 calculations
history_frame = Frame(window, width=312, height=100, bg="black")
history_frame.pack(side=RIGHT)

history_label = Label(history_frame, text="", fg="white", bg="black", font=('arial', 12))
history_label.pack(fill="both", expand=True)

window.config(bg="black", menu=menubar)
window.mainloop()
