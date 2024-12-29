import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("400x400")

        # variables
        self.celsius_var = ctk.StringVar(value="0")
        self.fahr_var = ctk.StringVar(value="0")

        # Widgets
        self.cel_text = ctk.CTkLabel(self, text="Celsius to Fahrenheit", justify="left", font=("Arial", 20))
        self.cel_frame = ctk.CTkFrame(self)
        self.cel_field = ctk.CTkEntry(self.cel_frame, textvariable=self.celsius_var, height=40, font=("Sans-serif", 30))
        self.cel_btn = ctk.CTkButton(self.cel_frame, text="Convert", height=40, font=("Sans-serif", 25),
                                     command=self.convert_to_fahr)
        self.cel_result = ctk.CTkLabel(self.cel_frame, font=("Sans-serif", 25), text="")

        self.fahr_text = ctk.CTkLabel(self, text="Fahrenheit to Celsius", justify="left", font=("Sans-serif", 20))
        self.fahr_frame = ctk.CTkFrame(self)
        self.fahr_field = ctk.CTkEntry(self.fahr_frame, textvariable=self.fahr_var, height=40, font=("Sans-serif", 30))
        self.fahr_btn = ctk.CTkButton(self.fahr_frame, text="Convert", height=40, font=("Sans-serif", 25),
                                      command=self.convert_to_celsius)
        self.fahr_result = ctk.CTkLabel(self.fahr_frame, font=("Sans-serif", 25), text="")

        # Packing
        self.cel_text.pack(anchor="w", padx=5, pady=5)
        self.cel_frame.pack(expand=True, fill="both")
        self.cel_field.pack(expand=True, fill="both")
        self.cel_btn.pack(fill="both")
        self.cel_result.pack()

        self.fahr_text.pack(anchor="w", padx=5, pady=5)
        self.fahr_frame.pack(expand=True, fill="both")
        self.fahr_field.pack(expand=True, fill="both")
        self.fahr_btn.pack(fill="both")
        self.fahr_result.pack()

        self.mainloop()

    def convert_to_fahr(self):
        try:
            result = str(round(float(self.celsius_var.get()) * (9 / 5) + 32, 2))
            self.cel_result.configure(text=str(result))
        except:
            self.cel_result.configure(text="Error")

    def convert_to_celsius(self):
        # C = (F - 32) * 5 / 9
        try:
            result = str(round((float(self.fahr_var.get()) - 32) * 5 / 9, 2))
            self.fahr_result.configure(text=str(result))
        except:
            self.fahr_result.configure(text="Error")



if __name__ == '__main__':
    app = App()
