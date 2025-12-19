import tkinter as tk
from tkinter import ttk

class MultiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyek Kolaborasi Python")
        self.geometry("500x350")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_tabs()

    def create_tabs(self):
        # Tab placeholder (akan diganti fitur anggota)
        frame = ttk.Frame(self.notebook)
        label = ttk.Label(frame, text="Fitur akan ditambahkan oleh anggota")
        label.pack(padx=20, pady=20)

        self.notebook.add(frame, text="Home")

if __name__ == "__main__":
    app = MultiApp()
    app.mainloop()
