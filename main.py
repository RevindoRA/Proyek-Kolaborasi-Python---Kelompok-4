import tkinter as tk
from tkinter import ttk

class MultiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyek Kolaborasi Python")
        self.geometry("400x300")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_tabs()

    def create_tabs(self):
        pass  # nanti diisi fitur anggota

if __name__ == "__main__":
    app = MultiApp()
    app.mainloop()
