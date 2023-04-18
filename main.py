from tkinter import *
import tkinter.messagebox as mb
import numpy as np

window = Tk()
window.title("Метод Гаусса/Итераций/Зейделя")
window.geometry("700x450")


def count_gauss():  # solve system with gauss method
    x1res.config(text="")
    x2res.config(text="")
    x3res.config(text="")

    try:
        line1 = [int(x11.get()), int(x12.get()), int(x13.get())]
        line2 = [int(x21.get()), int(x22.get()), int(x23.get())]
        line3 = [int(x31.get()), int(x32.get()), int(x33.get())]

        a = [line1, line2, line3]
        b = [int(b1.get()), int(b2.get()), int(b3.get())]

        x = np.linalg.solve(a, b)
        x1res.config(text=f"X1 = {round(x[0])}")
        x2res.config(text=f"X2 = {round(x[1])}")
        x3res.config(text=f"X3 = {round(x[2])}")
    except:
        mb.showerror("Ошибка", "Решения не найдены. Убедитесь, что вы ввели значения верно (это система с 3 переменными!!)")


def count_iteration():  # solve system with iteration method
    x1res.config(text="")
    x2res.config(text="")
    x3res.config(text="")

    try:
        line1 = [int(x11.get()), int(x12.get()), int(x13.get())]
        line2 = [int(x21.get()), int(x22.get()), int(x23.get())]
        line3 = [int(x31.get()), int(x32.get()), int(x33.get())]

        a = [line1, line2, line3]
        b = [int(b1.get()), int(b2.get()), int(b3.get())]

    except:
        mb.showerror("Ошибка",
                     "Решения не найдены. Убедитесь, что вы ввели значения верно (это система с 3 переменными!!)")


def count_zeidel():  # solve system with zeidel method
    x1res.config(text="")
    x2res.config(text="")
    x3res.config(text="")

    try:
        line1 = [int(x11.get()), int(x12.get()), int(x13.get())]
        line2 = [int(x21.get()), int(x22.get()), int(x23.get())]
        line3 = [int(x31.get()), int(x32.get()), int(x33.get())]

        a = [line1, line2, line3]
        b = [int(b1.get()), int(b2.get()), int(b3.get())]

    except:
        mb.showerror("Ошибка",
                     "Решения не найдены. Убедитесь, что вы ввели значения верно (это система с 3 переменными!!)")


# first line


label1a1 = Label(window, text="a1=", font=("Calibri", 15), fg="white")
label1a1.grid(column=2, row=2, pady=10, sticky=W)

x11 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x11.grid(column=3, row=2, sticky=W)

label1x11 = Label(window, text="X1", font=("Calibri", 19), fg="white")
label1x11.grid(column=4, row=2, sticky=W)

labelplus11 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus11.grid(column=5, row=2, sticky=W)

label1a21 = Label(window, text="a2=", font=("Calibri", 15), fg="white")
label1a21.grid(column=6, row=2, pady=10,sticky=W)

x12 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x12.grid(column=7, row=2, sticky=W)

label1x21 = Label(window, text="X2", font=("Calibri", 19), fg="white")
label1x21.grid(column=8, row=2, sticky=W)

labelplus12 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus12.grid(column=9, row=2, sticky=W)

label1a3 = Label(window, text="a3=", font=("Calibri", 15), fg="white")
label1a3.grid(column=10, row=2, pady=10,sticky=W)

x13 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x13.grid(column=11, row=2, sticky=W)

label1x31 = Label(window, text="X3", font=("Calibri", 19), fg="white")
label1x31.grid(column=12, row=2, sticky=W)

labelequal1 = Label(window, text="  =  ", font=("Calibri", 24), fg="white")
labelequal1.grid(column=13, row=2, sticky=W)

label1b1 = Label(window, text="b1=", font=("Calibri", 15), fg="white")
label1b1.grid(column=14, row=2, pady=10,sticky=W)

b1 = Entry(window, font=("Calibri", 23), validate="key", width=4)
b1.grid(column=15, row=2, sticky=W)


# second line


label2a1 = Label(window, text="a1=", font=("Calibri", 15), fg="white")
label2a1.grid(column=2, row=3, pady=10, sticky=W)

x21 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x21.grid(column=3, row=3, sticky=W)

label1x21 = Label(window, text="X1", font=("Calibri", 19), fg="white")
label1x21.grid(column=4, row=3, sticky=W)

labelplus21 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus21.grid(column=5, row=3, sticky=W)

label1a22 = Label(window, text="a2=", font=("Calibri", 15), fg="white")
label1a22.grid(column=6, row=3, pady=10, sticky=W)

x22 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x22.grid(column=7, row=3, sticky=W)

label1x22 = Label(window, text="X2", font=("Calibri", 19), fg="white")
label1x22.grid(column=8, row=3, sticky=W)

labelplus22 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus22.grid(column=9, row=3, sticky=W)

label1a3 = Label(window, text="a3=", font=("Calibri", 15), fg="white")
label1a3.grid(column=10, row=3, pady=10, sticky=W)

x23 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x23.grid(column=11, row=3, sticky=W)

label1x31 = Label(window, text="X3", font=("Calibri", 19), fg="white")
label1x31.grid(column=12, row=3, sticky=W)

labelequal2 = Label(window, text="  =  ", font=("Calibri", 24), fg="white")
labelequal2.grid(column=13, row=3, sticky=W)

label1b1 = Label(window, text="b1=", font=("Calibri", 15), fg="white")
label1b1.grid(column=14, row=3, pady=10, sticky=W)

b2 = Entry(window, font=("Calibri", 23), validate="key", width=4)
b2.grid(column=15, row=3, sticky=W)


# third line


label3a1 = Label(window, text="a1=", font=("Calibri", 15), fg="white")
label3a1.grid(column=2, row=4, pady=10, sticky=W)

x31 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x31.grid(column=3, row=4, sticky=W)

label1x31 = Label(window, text="X1", font=("Calibri", 19), fg="white")
label1x31.grid(column=4, row=4, sticky=W)

labelplus31 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus31.grid(column=5, row=4, sticky=W)

label1a32 = Label(window, text="a2=", font=("Calibri", 15), fg="white")
label1a32.grid(column=6, row=4, pady=10, sticky=W)

x32 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x32.grid(column=7, row=4, sticky=W)

label1x32 = Label(window, text="X2", font=("Calibri", 19), fg="white")
label1x32.grid(column=8, row=4, sticky=W)

labelplus32 = Label(window, text="  +  ", font=("Calibri", 24), fg="white")
labelplus32.grid(column=9, row=4, sticky=W)

label1a33 = Label(window, text="a3=", font=("Calibri", 15), fg="white")
label1a33.grid(column=10, row=4, pady=10, sticky=W)

x33 = Entry(window, font=("Calibri", 23), validate="key", width=4)
x33.grid(column=11, row=4, sticky=W)

label1x33 = Label(window, text="X3", font=("Calibri", 19), fg="white")
label1x33.grid(column=12, row=4, sticky=W)

labelequal3 = Label(window, text="  =  ", font=("Calibri", 24), fg="white")
labelequal3.grid(column=13, row=4, sticky=W)

label1b3 = Label(window, text="b1=", font=("Calibri", 15), fg="white")
label1b3.grid(column=14, row=4, pady=10, sticky=W)

b3 = Entry(window, font=("Calibri", 23), validate="key", width=4)
b3.grid(column=15, row=4, sticky=W)


# result line

x1res = Label(window, font=("Calibri", 20), fg="white")
x2res = Label(window, font=("Calibri", 20), fg="white")
x3res = Label(window, font=("Calibri", 20), fg="white")

x1res.grid(column=3, row=8, sticky=W, columnspan=4)
x2res.grid(column=3, row=9, sticky=W, columnspan=4)
x3res.grid(column=3, row=10, sticky=W, columnspan=4)


# other elements


label = Label(window, width=2)
label.grid(column=1, row=1)

btnCount_gauss = Button(text="Рассчитать Гаусса", font=("Calibri", 22), command=count_gauss, width=18)
btnCount_gauss.grid(column=0, row=5, columnspan=20, pady=6)

btnCount_iter = Button(text="Рассчитать Итерациями", font=("Calibri", 22), command=count_iteration, width=18)
btnCount_iter.grid(column=0, row=6, columnspan=20, pady=6)

btnCount_zeid = Button(text="Рассчитать Зейделем", font=("Calibri", 22), command=count_zeidel, width=18)
btnCount_zeid.grid(column=0, row=7, columnspan=20, pady=6)

window.mainloop()
