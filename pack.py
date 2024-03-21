from tkinter import *
from tkinter import ttk


root=Tk()
root.geometry("300x300")


frame1=ttk.Frame(root,relief="solid",padding=(12,12))
frame1.grid()


answerbox=ttk.Button(frame1,text="Answer")
answerbox.pack()

frame2=ttk.Frame(root,relief="solid",padding=(12,12))
frame2.grid()

btn1=ttk.Button(frame2,text="Button 2")
btn1.pack()

#can put the name of the side lowercase in quotes

root.mainloop()