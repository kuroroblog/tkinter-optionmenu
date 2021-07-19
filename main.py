import tkinter as tk

class Application(tk.Frame):
    # optionmenu Widget内の選択肢が選択された場合に、実行する関数
    def getSelectedValue(self, value):
        # 選択した選択肢の値を出力する。
        print(value)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 現在選択されているoptionmenu Widget内の選択肢の値を、文字列変数として扱う。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        var = tk.StringVar()
        # set() : 初期値としてaaaの値を設定する。
        var.set('aaa')

        # frame Widget(Frame)を親要素として、optionmenu Widgetを作成する。
        # var : 現在選択されている選択肢の値。文字列変数(var)として値を持たせることで、可変として扱う。
        # 'aaa', 'bbb' : 選択肢1, 選択肢2
        # command : optionmenu Widget内の選択肢が選択された場合に、実行する関数を設定。self.getSelectedValueとする。
        optionmenu = tk.OptionMenu(frame, var, 'aaa', 'bbb', command=self.getSelectedValue)

        # frame Widget(Frame)を親要素とした場合に、optionmenu Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        optionmenu.pack()


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # WIndowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
