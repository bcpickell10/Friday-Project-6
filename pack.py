import tkinter as tk

def append_to_display(value):
    entry_text.set(entry_text.get() + value)

def clear_display():
    entry_text.set("")

def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(str(result))
    except Exception as e:
        entry_text.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, state='disabled')
entry.pack(fill='x')

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(button_frame, text=button, width=5, height=2,
              command=lambda b=button: append_to_display(b)).grid(row=row, column=col, padx=1, pady=1)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(button_frame, text='C', width=5, height=2, command=clear_display).grid(row=row, column=0, padx=1, pady=1)
tk.Button(button_frame, text='=', width=5, height=2, command=calculate).grid(row=row, column=1, columnspan=3, padx=1, pady=1)

root.mainloop()
