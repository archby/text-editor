import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Editor")
root.geometry("1000x450")
root.aspect(20, 9, 20, 9)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

text_area = tk.Text(
    root,
    wrap=tk.WORD,
    bg="#1e1e1e",
    fg="#d4d4d4",
    insertbackground="white",
    font=("Courier", 12),
    padx=10,
    pady=10
)
text_area.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

root.mainloop()