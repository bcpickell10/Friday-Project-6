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

btn0=ttk.Button(frame2,text="0")
btn0.pack()
btn1=ttk.Button(frame2,text="1")
btn1.pack()
btn2=ttk.Button(frame2,text="2")
btn2.pack()
btn3=ttk.Button(frame2,text="3")
btn3.pack()
btn4=ttk.Button(frame2,text="4")
btn4.pack()
btn5=ttk.Button(frame2,text="5")
btn5.pack()
btn6=ttk.Button(frame2,text="6")
btn6.pack()
btn7=ttk.Button(frame2,text="7")
btn7.pack()
btn8=ttk.Button(frame2,text="8")
btn8.pack()
btn9=ttk.Button(frame2,text="9")
btn9.pack()
#can put the name of the side lowercase in quotes

root.mainloop()