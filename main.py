import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

root = tk.Tk()
root.title("Text Editor")
root.geometry("1000x450")
root.aspect(20, 9, 20, 9)

current_file_path = None

def update_window_title():
    global current_file_path
    if current_file_path:
        file_name = os.path.basename(current_file_path)
        root.title(f"Text Editor - {file_name}")
    else:
        root.title("Text Editor - New Document")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit? Make sure you saved!"):
        root.destroy()
def on_save_button_click():
    global current_file_path
    retrieved_text = text_area.get("1.0", "end-1c")

    if current_file_path is None:
        selected_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if selected_file:
            current_file_path = selected_file
        else:
            return
    with open(current_file_path, "w") as file:
        file.write(retrieved_text)
    update_window_title()
    messagebox.showinfo("Saved", "File saved successfully!")
def on_new_button_click():
    global current_file_path
    if messagebox.askyesno("New File", "Are you sure you want to open a new document? Unsaved changes will be lost."):
        text_area.delete("1.0", tk.END)
        current_file_path = None
        update_window_title()
def on_open_button_click():
    global current_file_path

    selected_file = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if selected_file:
        current_file_path = selected_file
        text_area.delete("1.0", tk.END)
        with open(current_file_path, "r") as file:
            text_area.insert("1.0", file.read())
        update_window_title()

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
    bg="#a3a3a3",
    fg="black"
)
save_button.pack(pady=5)

new_button = tk.Button(
    root,
    text="New",
    command=on_new_button_click,
    bg="#a3a3a3",
    fg="black"
)

new_button.pack(pady=5)

open_button = tk.Button(
    root,
    text="Open",
    command=on_open_button_click,
    bg="#a3a3a3",
    fg="black",
)
open_button.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()