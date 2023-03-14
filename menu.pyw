from tkinter import *

root = Tk()


# Функции
# функция,меняющая шрифт
def change_font(font):
    entry.config(font=('Arial', font))


entry_appearance = False


def option_entry_on():
    global entry, entry_appearance
    if entry_appearance == False:
        entry = Entry(width=15)
        entry.insert(0, "Февралева")
        entry.place(x=220, y=150)
        entry.bind("<Button-3>", self)
        entry_appearance = True


def option_entry_disabling():
    global entry, entry_appearance
    if entry_appearance:
        entry.place_forget()
        entry_appearance = False


def on_keyboard_shortcutson(event):
    global entry, entry_appearance
    if entry_appearance == False:
        entry = Entry(width=15)
        entry.insert(0, "Февралева")
        entry.place(x=220, y=150)
        entry.bind("<Button-1>", self)
        entry_appearance = True


def off_keyboard_shortcuts(event):
    global entry, entry_appearance
    if entry_appearance:
        entry.place_forget()
        entry_appearance = False


def self(event):
    selfmenu.post(event.x_root, event.y_root)


# Горячие клавиши
root.bind("<z>", on_keyboard_shortcutson)
root.bind("<x>", off_keyboard_shortcuts)

# Контекстное меню
selfmenu = Menu(tearoff=0)
selfmenu.add_radiobutton(label="5", command=lambda: change_font(5))
selfmenu.add_radiobutton(label="10", command=lambda: change_font(10))
selfmenu.add_radiobutton(label="15", command=lambda: change_font(15))
selfmenu.add_radiobutton(label="20", command=lambda: change_font(20))
selfmenu.add_radiobutton(label="25", command=lambda: change_font(25))

# Окно
root.geometry("500x300")
root.title("Персонал")

# Картинки для меню
on_button= PhotoImage(file="on_button.png")
off_button = PhotoImage(file="off_button.png")

# Меню
mainmenu = Menu(root)
root.config(menu=mainmenu)

isaev_progect=Menu(mainmenu,tearoff=0)
isaev_progect.add_command(label='SuperDoctor')



#  flutter developers_progects
isaev_progect=Menu(mainmenu,tearoff=0)
isaev_progect.add_command(label='SuperDoctor')
# c
petrov_progect=Menu(mainmenu,tearoff=0)
petrov_progect.add_command(label="MegaBank-onlain banking")

ivanova_progect=Menu(mainmenu,tearoff=0)
ivanova_progect.add_command(label="Vikings_GreatWAR")

c_devs_date=Menu(mainmenu,tearoff=0)
c_devs_date.add_cascade(label="Петров П.П.",menu=petrov_progect)
c_devs_date.add_cascade(label="Иванова И.И.",menu=ivanova_progect)
#js
fedotova_progect=Menu(mainmenu,tearoff=0)
fedotova_progect.add_command(label="kids")
js_devs_date=Menu(mainmenu,tearoff=0)
js_devs_date.add_cascade(label="Федотова А.А.",menu=fedotova_progect)
# go
sidorov_progect=Menu(mainmenu,tearoff=0)
sidorov_progect.add_command(label='Supermarket')
go_devs_date=Menu(mainmenu,tearoff=0)
go_devs_date.add_cascade(label="Сидоров С.П.",menu=sidorov_progect)
go_devs_date.add_command(label="Иванова И.И.")


flutter_devs_date = Menu(mainmenu, tearoff=0)
flutter_devs_date.add_cascade(label='Исаев В.В.', menu=isaev_progect)


dev_departments = Menu(mainmenu, tearoff=0)
dev_departments.add_cascade(label='C',menu=c_devs_date)
dev_departments.add_cascade(label='IOS',menu=js_devs_date)
dev_departments.add_cascade(label='Go',menu=go_devs_date)
dev_departments.add_separator()
dev_departments.add_cascade(label='Fluter...', menu=flutter_devs_date)

#ui progects
petrova_progects=Menu(mainmenu,tearoff=0)
petrova_progects.add_command(label='SuperDoctor')
petrova_progects.add_command(label='SuperBank-onlain banking')

sidorova_progect=Menu(mainmenu,tearoff=0)
sidorova_progect.add_command(label='Vikings_GreatWar')
sidorova_progect.add_command(label='SuperMarket')

ui=Menu(mainmenu,tearoff=0)
ui.add_cascade(label="Петрова И.А.",menu=petrova_progects)
ui.add_cascade(label="Сидорова А.А.",menu=sidorova_progect)

ux_progects=Menu(mainmenu,tearoff=0)
pet_progects=Menu(mainmenu,tearoff=0)
pet_progects.add_command(label='SuperDoctor')
pet_progects.add_command(label='SuperBank-onlain banking')

sidokova_progect=Menu(mainmenu,tearoff=0)
sidokova_progect.add_command(label='Vikings_GreatWar')
sidokova_progect.add_command(label='SuperMarket')

ux=Menu(mainmenu,tearoff=0)
ux.add_cascade(label="Пет А.О.",menu=pet_progects)
ux.add_cascade(label="Сидокова О.А.",menu=sidokova_progect)


designers = Menu(mainmenu, tearoff=0)
designers.add_cascade(label='UI', menu=ui)
designers.add_cascade(label='UX', menu=ux)
designers.add_command(label='Game designers')

#qa
  #qa progects
ilina_progect=Menu(mainmenu,tearoff=0)
ilina_progect.add_command(label="SuperDoctor")

frolova_progect=Menu(mainmenu,tearoff=0)
frolova_progect.add_command(label="kids")

evkova_progect=Menu(mainmenu,tearoff=0)
evkova_progect.add_command(label='SuperMarket')

ivankova_progect=Menu(mainmenu,tearoff=0)
ivankova_progect.add_command(label="Megabank-olain bank")

qa_department=Menu(mainmenu,tearoff=0)
qa_department.add_cascade(label="Илина и.и.",menu=ilina_progect)
qa_department.add_cascade(label="Фролова Ф.Е.",menu=frolova_progect)
qa_department.add_cascade(label="Евкова П.Е.",menu=evkova_progect)
qa_department.add_cascade(label="Иванкова И.И.",menu=ivankova_progect)

# disiners


autor_date_condition=Menu(mainmenu,tearoff=0)
autor_date_condition.add_command(label='on',image=on_button,  compound=LEFT, command=option_entry_on, accelerator="z")
autor_date_condition.add_command(label='off', image=off_button, compound=LEFT, command=option_entry_disabling(),accelerator="x")
supplement=Menu(mainmenu,tearoff=0)

about_autor=Menu(mainmenu,tearoff=0)
about_autor.add_cascade(label="Об авторе",menu=supplement)
autor_date=Menu(mainmenu,tearoff=0)
autor_date.add_cascade(label="Kbxyst lfyuyst",menu=autor_date_condition)
autor_date_condition=Menu(mainmenu,tearoff=0)
autor_date_condition.add_command(label='on',image=on_button,  compound=LEFT, command=option_entry_on, accelerator="z")
autor_date_condition.add_command(label='off', image=off_button, compound=LEFT, command=option_entry_disabling,accelerator="x")


autor_date=Menu(mainmenu,tearoff=0)
autor_date.add_cascade(label="об авторе",menu=autor_date_condition)



supplement=Menu(mainmenu,tearoff=0)


mainmenu.add_cascade(label='Отдел разработки', menu=dev_departments)
mainmenu.add_cascade(label='Отдел тестирования' ,menu=qa_department)
mainmenu.add_cascade(label='Дизайнеры', menu=designers)
mainmenu.add_cascade(label="Дополнительно",menu=autor_date)
root.mainloop()
