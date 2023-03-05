from tkinter import *
from tkinter import ttk, messagebox
import sys

class TextEdit:
    def __init__(self, root):
        root.title(self.__class__.__name__)
        root.geometry('300x50')

        root.option_add("*tearoff", FALSE)
        menu = Menu()
        menuFile = Menu()
        menu.add_cascade(menu=menuFile, label="ファイル(F)")
        menuFile.add_command(label="終了(X)",command=self.menuFileExit)
        menuHelp = Menu()
        menu.add_cascade(menu=menuHelp, label="ヘルプ(H)", underline=4)
        menuHelp.add_command(label="バージョン情報(V)", underline=8, command=self.menuHelpVersion)
        root["menu"] = menu

    def menuFileExit(self):
        root.destroy()

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += "Version 0.01(2021/03/10)\n"
        s += "@2021 Hideo Harada\n"
        s += "with Python " + sys.version
        messagebox.showinfo(self.__class__.__name__, s)

root = Tk()
TextEdit(root)
root.mainloop()