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

# Set custom font for the labels
font = ("Arial", 12)

# Title
tk.Label(root, text="Sign Up", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Name:", font=font).grid(row=1, column=0, sticky='e')
tk.Label(root, text="Email:", font=font).grid(row=2, column=0, sticky='e')
tk.Label(root, text="Password:", font=font).grid(row=3, column=0, sticky='e')

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

name_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
password_entry.grid(row=3, column=1)

# Make the Sign Up button span across two columns
sign_up_button = tk.Button(root, text="Sign Up Now", command=sign_up)
sign_up_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
