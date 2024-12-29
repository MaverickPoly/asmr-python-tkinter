import tkinter as tk
from tkinter import ttk
import string
import random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random password generator")
        self.geometry("500x500")

        self.scale_var = tk.IntVar(value=8)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.punctuation_var = tk.BooleanVar(value=True)

        self.frame = ttk.Frame(self)
        self.heading = ttk.Label(self.frame, text="Random password generator app", font=("Calibri", 20))
        self.slider = ttk.Scale(self.frame, from_=8, to=30, variable=self.scale_var)
        self.btn = ttk.Button(self.frame, text="Generate", command=self.generate_password)
        self.scale_text = ttk.Label(self.frame, textvariable=self.scale_var)
        self.frame.grid(row=1, column=1)
        self.heading.pack(pady=20, padx=20)
        self.slider.pack(padx=20, pady=20)
        self.scale_text.pack()
        self.btn.pack()

        self.check_frame = ttk.Frame(self)
        self.check_uppercase = ttk.Checkbutton(self.check_frame, text="Uppercase", variable=self.upper_var)
        self.check_lowercase = ttk.Checkbutton(self.check_frame, text="Lowercase", variable=self.lower_var)
        self.check_digits = ttk.Checkbutton(self.check_frame, text="Digits", variable=self.digit_var)
        self.check_punctuation = ttk.Checkbutton(self.check_frame, text="Punctuations", variable=self.punctuation_var)
        self.check_uppercase.pack(side="left", pady=10)
        self.check_lowercase.pack(side="left", pady=10)
        self.check_digits.pack(side="left", pady=10)
        self.check_punctuation.pack(side="left", pady=10)
        self.check_frame.grid(row=2, column=1)

        self.result = ttk.Label(self, text="Password will appear here...", font=("Arial", 16))
        self.result.grid(row=3, column=1)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(1, weight=1)
        self.mainloop()

    def generate_password(self):
        combinations = ""
        if self.upper_var.get():
            combinations += string.ascii_uppercase
        if self.lower_var.get():
            combinations += string.ascii_lowercase
        if self.digit_var.get():
            combinations += string.digits
        if self.punctuation_var.get():
            combinations += string.punctuation
        password = "".join(random.choices(combinations or "-", k=self.scale_var.get()))
        self.result.configure(text=password)



if __name__ == '__main__':
    App()
