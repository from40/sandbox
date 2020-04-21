from tkinter import *

root = Tk()
root.title("Title")
root.geometry("600x350+600+300")
root.resizable(width=False, height=False)



btn1 = Button(text="СЕВЕР", background="#0000FF", foreground="#fff",
              pady="2", font="12", width=12)
btn1.pack(side=TOP)
btn2 = Button(text="ЮГ", background="#FF4500", foreground="#fff",
              pady="2", font="12", width=12)
btn2.pack(side=BOTTOM)
btn3 = Button(text="ЗАПАД", background="#000000", foreground="#fff",
              pady="2", font="12", width=12)
btn3.pack(side=LEFT)
btn4 = Button(text="ВОСТОК", background="#008000", foreground="#fff",
              pady="2", font="12", width=12)
btn4.pack(side=RIGHT)
label = Label(text="Куда идти?", font="12", pady="140")
label.pack()


root.mainloop()
