import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Text Editor")
root.geometry("1000x450")
root.aspect(20, 9, 20, 9)

def on_closing():
    # Quick pop-up asking if they want to exit
    if messagebox.askokcancel("Quit", "Do you want to quit? Make sure you saved!"):
        root.destroy()

def on_save_button_click():
    retrieved_text = text_area.get("1.0", "end-1c")
    wsave = str(input("Where to save? (TXT FILE): "))
    with open(f"{wsave}.txt", "w") as file:
        file.write(retrieved_text)
def on_new_button_click():
    name = str(input("Name of the file? (WILL CREATE A TXT FILE): "))
    f = open(f"{name}.txt", "x")
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
text_area.insert("1.0", "Type anything...")

save_button = tk.Button(
    root,
    text="Save",
    command=on_save_button_click,
    bg="#007acc",
    fg="black"
)
save_button.pack(pady=5)

new_button = tk.Button(
    root,
    text="New",
    command=on_new_button_click,
    bg="#007acc",
    fg="black"
)

new_button.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()