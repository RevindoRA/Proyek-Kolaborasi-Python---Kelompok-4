import tkinter as tk
from tkinter import ttk, messagebox


class MultiApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Serba Guna")
        self.geometry("400x500")
        self.resizable(False, False)

        self.create_tabs()

    def create_tabs(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Tab
        self.calc_tab = ttk.Frame(notebook)
        self.currency_tab = ttk.Frame(notebook)
        self.height_tab = ttk.Frame(notebook)

        notebook.add(self.calc_tab, text="Kalkulator")
        notebook.add(self.currency_tab, text="Mata Uang")
        notebook.add(self.height_tab, text="Tinggi Badan")

        self.create_calculator()
        self.create_currency_converter()
        self.create_height_converter()

    # =======================
    # KALKULATOR
    # =======================
    def create_calculator(self):
        self.expression = ""
        self.calc_display = tk.StringVar()

        display = ttk.Entry(
            self.calc_tab,
            textvariable=self.calc_display,
            font=("Arial", 18),
            justify="right"
        )
        display.pack(fill="x", padx=10, pady=10, ipady=10)

        frame = ttk.Frame(self.calc_tab)
        frame.pack(expand=True, fill="both")

        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
            ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
        ]

        clear = ttk.Button(frame, text="C", command=self.clear_calc)
        clear.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        for (text, r, c) in buttons:
            ttk.Button(
                frame,
                text=text,
                command=lambda t=text: self.calc_click(t)
            ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(4):
            frame.columnconfigure(j, weight=1)

    def calc_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                self.calc_display.set(result)
                self.expression = str(result)
            except:
                messagebox.showerror("Error", "Perhitungan tidak valid")
                self.clear_calc()
        else:
            self.expression += char
            self.calc_display.set(self.expression)

    def clear_calc(self):
        self.expression = ""
        self.calc_display.set("")

    # =======================
    # KONVERSI MATA UANG
    # =======================
    def create_currency_converter(self):
        frame = ttk.Frame(self.currency_tab, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Jumlah").pack(pady=5)
        self.currency_amount = tk.DoubleVar()
        ttk.Entry(frame, textvariable=self.currency_amount).pack()

        ttk.Label(frame, text="Rate (contoh: 1 USD = 15500 IDR)").pack(pady=5)
        self.currency_rate = tk.DoubleVar()
        ttk.Entry(frame, textvariable=self.currency_rate).pack()

        ttk.Button(frame, text="Konversi", command=self.convert_currency).pack(pady=10)

        self.currency_result = ttk.Label(frame, text="Hasil: -", font=("Arial", 12))
        self.currency_result.pack(pady=10)

    def convert_currency(self):
        try:
            result = self.currency_amount.get() * self.currency_rate.get()
            self.currency_result.config(text=f"Hasil: {result:,.2f}")
        except:
            messagebox.showerror("Error", "Input tidak valid")

    # =======================
    # KONVERSI TINGGI BADAN
    # =======================
    def create_height_converter(self):
        frame = ttk.Frame(self.height_tab, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Tinggi").pack(pady=5)
        self.height_value = tk.DoubleVar()
        ttk.Entry(frame, textvariable=self.height_value).pack()

        self.height_type = tk.StringVar(value="ft_to_cm")
        ttk.Radiobutton(
            frame, text="Feet → CM",
            variable=self.height_type,
            value="ft_to_cm"
        ).pack()

        ttk.Radiobutton(
            frame, text="CM → Feet",
            variable=self.height_type,
            value="cm_to_ft"
        ).pack()

        ttk.Button(frame, text="Konversi", command=self.convert_height).pack(pady=10)

        self.height_result = ttk.Label(frame, text="Hasil: -", font=("Arial", 12))
        self.height_result.pack(pady=10)

    def convert_height(self):
        try:
            value = self.height_value.get()
            if self.height_type.get() == "ft_to_cm":
                result = value * 30.48
                self.height_result.config(text=f"Hasil: {result:.2f} cm")
            else:
                result = value / 30.48
                self.height_result.config(text=f"Hasil: {result:.2f} ft")
        except:
            messagebox.showerror("Error", "Input tidak valid")


if __name__ == "__main__":
    app = MultiApp()
    app.mainloop()
