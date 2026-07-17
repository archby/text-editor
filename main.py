import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Editor")
root.geometry("1000x450")
root.aspect(20, 9, 20, 9)

def on_save_button_click():
    retrieved_text = text_area.get("1.0", "end-1c")
    with open("file.txt", "w") as file:
        file.write(retrieved_text)
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

save_button = tk.Button(
    root,
    text="Save",
    command=on_save_button_click,
    bg="#007acc",
    fg="black"
)
save_button.pack(pady=5)

root.mainloop()