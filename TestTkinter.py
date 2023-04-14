from tkinter import *
from tkinter import messagebox
class Test:
    def __init__(self, main):
        main.title(self.__class__.__name__)
        main.geometry("300x300")
        main.option_add("*tearOff", FALSE)

        menubar = Menu()
        main["menu"] = menubar
        menuTest = Menu()
        menubar.add_cascade(menu=menuTest, label="Test(T)", underline=5)
        menuTest.add_command(label="Test(T)", underline=5, command=self.test)

    def test(self):
        messagebox.showinfo(self.__class__.__name__, "Test")

main = Tk()
Test(main)
main.mainloop()