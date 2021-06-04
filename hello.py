# Tkinterライブラリのインポート
import tkinter as tk

root = tk.Tk()
# 常に最前表示
root.attributes("-topmost", True)
root.title("すぐぐる")
root.geometry("420x40")
label = tk.Label(root, text="")
label.pack()
# テキストボックス
txt = tk.Entry(width=65)
txt.place(x=10, y=10)
# エンターで検索処理
root.bind('<Return>', app.callback)
root.mainloop()
