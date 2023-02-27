from tkinter import *
from tkinter import ttk

class TextEdit:
    def __init__(self, root):
        root.title(self.__class__.__name__)
        root.geometry("300x50")

        root.option_add("tearoff", FALSE)
        menu = Menu()
        menuFile = Menu()
        menu.add_cascade(menu=menuFile, label="ファイル(F)", underline=5)
        menuFile.add_command(label="終了(X)", underline=3, command=self.menuFileExit)
        root["menu"] = menu

    def menuFileExit(self):
        root.destroy()

root = Tk()
TextEdit(root)
root.mainloop()