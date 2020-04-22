from tkinter import *

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
user_entry.pack()

user_button = Button(root, text="Преобразовать")
user_button.pack()

user_label = Label(root, bg='black', fg='white', width=20)
user_label.pack()


def sortingImput(event):
    text = user_entry.get()
    text.replace(",", " ").split(" ").sort()
    user_label["text"] = "".join(text)

user_button.bind('<Button-1>', sortingImput)





# btn1 = Button(text="СЕВЕР", background="#0000FF", foreground="#fff",
#               pady="2", font="12", width=12)
# btn1.pack(side=TOP)


root.mainloop()
