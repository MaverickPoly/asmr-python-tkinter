import customtkinter as ctk


ctk.set_default_color_theme("green")
ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Variables
        self.kg_input_var = ctk.StringVar(value="")
        self.kg_res_var = ctk.StringVar(value="")
        self.pound_res_var = ctk.StringVar(value="")
        self.pound_input_var = ctk.StringVar(value="")

        # KG
        self.build_frame("Convert to Pounds", self.kg_to_pounds, self.kg_input_var, self.kg_res_var, "KG")
        # Pounds
        self.build_frame("Convert to KG", self.pounds_to_kg, self.pound_input_var, self.pound_res_var, "Pounds")
        # Theme toggle
        ctk.CTkButton(self, text="T", command=self.toggle_theme, width=30, height=30).place(relx=0.01, rely=0.01, anchor="nw")


        self.mainloop()

    def build_frame(self, btn_text, command, input_var, res_var, placeholder_text):
        frame = ctk.CTkFrame(self)
        input = ctk.CTkEntry(frame, textvariable=input_var, placeholder_text=placeholder_text)
        btn = ctk.CTkButton(frame, text=btn_text, command=command)
        res = ctk.CTkLabel(frame, textvariable=res_var, font=("Arial", 30))
        
        frame.pack(expand=True, fill="both")
        input.grid(row=1, column=1, padx=14, sticky="ew")
        btn.grid(row=1, column=2, padx=14, sticky="nsew", pady=20)
        res.grid(row=1, column=3, padx=14)

        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)

    def kg_to_pounds(self):
        pounds = round(float(self.kg_input_var.get()) * 2.205, 1)
        print(pounds)
        self.kg_res_var.set(str(pounds))

    def pounds_to_kg(self):
        kgs = round(float(self.pound_input_var.get()) / 2.205, 1)
        print(kgs)
        self.pound_res_var.set(str(kgs))

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")



if __name__ == "__main__":
    App()
