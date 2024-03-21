from tkinter import *
from tkinter import ttk


root=Tk()
root.geometry("300x300")


frame1=ttk.LabelFrame(root,relief="solid",text="Answer",padding=(12,12))
frame1.pack()


answerbox=ttk.Button(frame1,text="Answer")
answerbox.pack()

frame2=ttk.Frame(root,relief="solid",padding=(20,20))
frame2.pack()

btn0=ttk.Button(frame2,text="0")
btn0.pack(side=LEFT)
btn2=ttk.Button(frame2,text="2")
btn2.pack(side=RIGHT)
btn1=ttk.Button(frame2,text="1")
btn1.pack(side=RIGHT)

btn3=ttk.Button(frame2,text="3")
btn3.pack(side=BOTTOM)


root.mainloop()