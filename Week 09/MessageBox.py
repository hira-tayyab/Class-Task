import tkinter as tk
from tkinter import messagebox

def message():
    messagebox.showinfo("test", "Test message")

root=tk.Tk()
root.title("Message Box")
root.geometry("300x200")


tk.Button( root, text="Messaage",command=message ).pack(pady=50)



root.mainloop()







