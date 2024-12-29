import tkinter as tk
from tkinter import messagebox


class CurrencyConverterApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x400")

        self.dollar_rate = 0.96  # 1 USD = 0.96 EUR
        self.euro_rate = 1.04  # 1 EUR = 1.04 USD

        self.dollar_label = tk.Label(self.root, text="Amount in USD:", font=("Arial", 16))
        self.dollar_label.pack(pady=10)

        self.dollar_entry = tk.Entry(self.root, font=("Arial", 16))
        self.dollar_entry.pack(pady=10)

        self.convert_button_dollar = tk.Button(self.root, text="Convert to EUR", font=("Arial", 16), command=self.convert_to_euro)
        self.convert_button_dollar.pack(pady=10)

        self.euro_label = tk.Label(self.root, text="Amount in EUR:", font=("Arial", 16))
        self.euro_label.pack(pady=10)

        self.euro_entry = tk.Entry(self.root, font=("Arial", 16))
        self.euro_entry.pack(pady=10)

        self.convert_button_euro = tk.Button(self.root, text="Convert to Dollar", font=("Arial", 16), command=self.convert_to_dollar)
        self.convert_button_euro.pack(pady=10)

    def convert_to_euro(self):
        dollar = self.dollar_entry.get()

        if not dollar:
            messagebox.showerror("Error", "Please enter an amount in USD.")
            return

        try:
            dollar = float(dollar)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of the dollars!")
            return

        result = dollar * self.dollar_rate
        self.euro_entry.delete(0, tk.END)
        self.euro_entry.insert(0, str(result))

    def convert_to_dollar(self):
        euro = self.euro_entry.get()

        if not euro:
            messagebox.showerror("Error", "Please enter an amount in EUR.")
            return

        try:
            euro = float(euro)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of the euros!")
            return

        result = euro * self.euro_rate
        self.dollar_entry.delete(0, tk.END)
        self.dollar_entry.insert(0, str(result))


if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
