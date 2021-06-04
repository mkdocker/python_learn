# tkinterのインポート
import tkinter as tk

# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("350x100")

# Runボタン設置
run_button = tk.Button(root, text = "Run")
run_button.place(x = 160, y = 40)

# Setボタン設置 <---追加したコード
set_button = tk.Button(root, text = "Set")
set_button.place(x = 300, y = 7)

# テキストボックス配置
input_box = tk.Entry(width = 40)
input_box.place(x = 10, y = 10)

# ステータスバー設置
statusbar = tk.Label(root, text = " No Data!!", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
statusbar.pack(side = tk.BOTTOM, fill = tk.X)

# ウインドウ状態の維持
root.mainloop()
