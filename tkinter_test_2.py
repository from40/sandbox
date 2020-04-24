from tkinter import *

# Инициализация главного окна
root = Tk()
root.title("Title")
root.geometry("600x350+600+300")
root.resizable(width=False, height=False)

# text frame for message to be coded / decoded
message_frame = Text(root, width=63, height=9, bg="white", fg="black", wrap=WORD)
message_frame.place(x=50, y=20)

# text frame for key word
keyword_frame = Entry(root, width=45, bg="white", fg="black")
keyword_frame.place(x=178, y=200)

puch = Button(root, text="Puch", background="#483D8B", foreground="#fff", width=12)
puch.place(x=170, y=260)
sova = Button(root, text="Sova", background="#483D8B", foreground="#fff", width=12)
sova.place(x=370, y=260)

root.mainloop()


"""
! Object declaration:
object_name = Object(master[, parameters])
object_name.pack()
object_name.place(x=10, y=10)

! Object: Text or Entry
(width=x, height=y, bg="", fg="", wrap=WORD)
.get() - возвращает
.insert() - вставляет
.delete() - удаляет

! Object: Button
(text="user_text", width=x, height=y, bg="", fg="", command=user_function)
.bind('<Button-1>', user_function)
"""
