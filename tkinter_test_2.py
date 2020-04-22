from tkinter import *

class Block:
    def __init__(self, master):
        self.user_entry = Entry(master, width = 20)
        self.user_button = Button(master, text="Push it")
        self.user_label = Label(master, bg="black", fg="white", width=20)
        self.user_entry.pack()
        self.user_button.pack()
        self.user_label.pack()
    def setFunc(self, func):
        self.user_button['command'] = eval('self.' + func)
    def sortingImput(self):
        text = self.user_entry.get()
        text.replace(",", " ").split(" ").sort()
        self.user_label["text"] = "".join(text)
    def strReverse(self):
        text = self.user_entry.get()
        text.split().reverse()
        self.user_label['text'] = ''.join(text)

root = Tk()

first_block = Block(root)
