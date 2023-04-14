from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import sys, webbrowser

class TextEdit:
    def __init__(self, root):
        root.title(self.__class__.__name__)
        root.geometry('500x300')

        root.option_add("*tearOff", FALSE)
        menu = Menu()
        root["menu"] = menu

        menuFile = Menu()
        menu.add_cascade(menu=menuFile, label="ファイル(F)", underline=5)
        menuFile.add_command(label="終了(X)", underline=3 ,command=self.menuFileExit)

        menuHelp = Menu()
        menu.add_cascade(menu=menuHelp, label="ヘルプ(H)", underline=4)
        menuHelp.add_command(label="バージョン情報(V)", underline=8, command=self.menuHelpVersion)
        menuHelp.add_command(label="Webサイトを開く(W)", underline=10, command=self.menuHelpOpenWeb)

        text = ScrolledText()
        text.pack(expand=1, fill=BOTH)

    def menuFileExit(self):
        root.destroy()

    def menuHelpVersion(self):
        s = self.__class__.__name__
        s += "Version 0.01(2021/03/10)\n"
        s += "@2021 Hideo Harada\n"
        s += "with Python " + sys.version
        messagebox.showinfo(self.__class__.__name__, s)

    def menuHelpOpenWeb(self):
        webbrowser.open("https://info.nikkeibp.co.jp/media/NSW/")

root = Tk()
TextEdit(root)
root.mainloop()