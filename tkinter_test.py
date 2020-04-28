from tkinter import *
# import tkinter as tk


# Инициализация главного окна
root = Tk()
root.title("Title")
root.geometry("600x350+600+300")
root.resizable(width=False, height=False)

# Создать виджеты и выполнить конфигурацию их свойств
# Определить события, на которые программа будет реагировать
# Определить обработчики событий (как программа будет реагировать)
# Расположить виджеты в главном окне
# Запустить цикл обработки событий


user_entry = Entry(root, width=20)
user_entry.place(x=20, y=15)

user_button = Button(root, text="Преобразовать")
user_button.place(x=30, y=45)

user_label = Label(root, bg='black', fg='white', width=30, height=8)
user_label.place(x=170, y=15)

def sortingImput(event):
    text = user_entry.get()
    text.replace(",", " ").split(" ").sort()
    user_label["text"] = "".join(text)

user_button.bind('<Button-1>', sortingImput)

root.mainloop()


############################################################
'''

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





'''
