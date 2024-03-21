import tkinter as tk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Perform sign up logic here
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

root = tk.Tk()
root.title("Sign Up Page")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky='e')
tk.Label(root, text="Email:").grid(row=1, column=0, sticky='e')
tk.Label(root, text="Password:").grid(row=2, column=0, sticky='e')

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

sign_up_button = tk.Button(root, text="Sign Up Now", command=sign_up)
sign_up_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
