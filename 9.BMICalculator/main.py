import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#ff8c42")
        self.title("BMI Calculator")
        self.geometry("400x400")
        self.iconbitmap("./icon.ico")

        # Variables
        self.res_var = ctk.DoubleVar()
        self.weight_var = ctk.DoubleVar(value=60)
        self.height_var = ctk.DoubleVar(value=170)
        self.status_var = ctk.StringVar(value="Good")
        self.weight_var.trace(mode="rwua", callback=self.calculate)
        self.height_var.trace(mode="rwua", callback=self.calculate)

        self.build_ui()

        self.mainloop()

    def build_ui(self):
        # Result frame
        self.res_frame = ctk.CTkFrame(self, fg_color="#ffa552")
        self.res_text = ctk.CTkLabel(self.res_frame, textvariable=self.res_var, font=("Arial", 35), text_color="white")
        self.status_text = ctk.CTkLabel(self.res_frame, textvariable=self.status_var, font=("Arial", 15),
                                        text_color="white")
        self.res_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.res_text.place(relx=0.5, rely=0.5, anchor="center")
        self.status_text.place(relx=0.05, rely=0.05, anchor="nw")

        # Weight Frame
        self.weight_frame = ctk.CTkFrame(self, fg_color="#ff6b35")
        self.minus_big = ctk.CTkButton(self.weight_frame, text="-", width=60, height=60, font=("Arial", 30),
                                       fg_color="#ff3d00", hover_color="#ff6230",
                                       command=lambda: self.handle_weight("-", "big"))
        self.minus_small = ctk.CTkButton(self.weight_frame, text="-", width=50, height=50, font=("Arial", 30),
                                         fg_color="#ff4500", hover_color="#ff5f24",
                                         command=lambda: self.handle_weight("-", "small"))
        self.plus_big = ctk.CTkButton(self.weight_frame, text="+", width=60, height=60, font=("Arial", 30),
                                      fg_color="#ff3d00", hover_color="#ff6230",
                                      command=lambda: self.handle_weight("+", "big"))
        self.plus_small = ctk.CTkButton(self.weight_frame, text="+", width=50, height=50, font=("Arial", 30),
                                        fg_color="#ff4500", hover_color="#ff5f24",
                                        command=lambda: self.handle_weight("+", "small"))
        self.weight_label = ctk.CTkLabel(self.weight_frame, textvariable=self.weight_var, font=("Arial", 30),
                                         text_color="white")

        self.weight_frame.grid(row=2, column=1, sticky="nsew", pady=10, padx=10)
        self.minus_big.grid(row=1, column=1, padx=5, pady=5)
        self.minus_small.grid(row=1, column=2, padx=5, pady=5)
        self.weight_label.grid(row=1, column=3, padx=5, pady=5)
        self.plus_small.grid(row=1, column=4, padx=5, pady=5)
        self.plus_big.grid(row=1, column=5, padx=5, pady=5)

        self.weight_frame.rowconfigure(1, weight=1)
        self.weight_frame.columnconfigure(1, weight=2)
        self.weight_frame.columnconfigure(2, weight=1)
        self.weight_frame.columnconfigure(3, weight=4)
        self.weight_frame.columnconfigure(4, weight=1)
        self.weight_frame.columnconfigure(5, weight=2)

        # Height Frame
        self.height_frame = ctk.CTkFrame(self, fg_color="#ff6b35", corner_radius=10)
        self.slider = ctk.CTkSlider(self.height_frame, variable=self.height_var, from_=100, to=200,
                                    command=self.on_slider_change, button_color="#ffa552", progress_color="#ff8c42",
                                    button_hover_color="#ffad78")
        self.height_label = ctk.CTkLabel(self.height_frame, text=str(self.height_var.get()), font=("Arial", 25),
                                         text_color="white")

        self.height_frame.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)
        self.slider.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.height_label.grid(row=1, column=2, padx=5, pady=5)

        self.height_frame.rowconfigure(1, weight=1)
        self.height_frame.columnconfigure(1, weight=4)
        self.height_frame.columnconfigure(2, weight=1)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def calculate(self, *args):
        result = self.weight_var.get() / ((self.height_var.get() / 100) ** 2)
        self.res_var.set(round(result, 1))

        if 10 < result < 20:
            self.status_var.set("Underweight")
        elif 30 < result < 40:
            self.status_var.set("Overweight")
        elif 40 < result:
            self.status_var.set("Very Overweight")
        elif result < 10:
            self.status_var.set("Very underweight")
        else:
            self.status_var.set("Good")


    def on_slider_change(self, *args):
        self.height_label.configure(text=round(self.height_var.get()))

    def handle_weight(self, sign, big):
        value = 2 if big == "big" else 0.5
        if sign == "+":
            self.weight_var.set(self.weight_var.get() + value)
        elif sign == "-" and self.weight_var.get() - value >= 0:
            self.weight_var.set(self.weight_var.get() - value)



if __name__ == '__main__':
    App()
