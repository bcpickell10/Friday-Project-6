import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Perform login logic here
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Login Page")

tk.Label(root, text="Username:").place(x=50, y=30)
tk.Label(root, text="Password:").place(x=50, y=60)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

username_entry.place(x=120, y=30)
password_entry.place(x=120, y=60)

login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=100, y=90)

root.mainloop()
