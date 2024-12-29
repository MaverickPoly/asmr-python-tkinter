import customtkinter as ctk
from tkinter import colorchooser


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Color picker")
        self.geometry("500x500")

        self.frame = ctk.CTkFrame(self)
        self.color_label = ctk.CTkLabel(self.frame)
        self.btn = ctk.CTkButton(self.frame, text="Choose Color", command=self.ask_color)
        self.bg_btn = ctk.CTkButton(self.frame, text="BG Color", command=self.ask_bg_color)
        self.bg_btn.pack(side="right", padx=20)
        self.frame.pack()
        self.color_label.pack(side="left")
        self.btn.pack()

        self.container = ctk.CTkFrame(self, width=200, height=200)
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.mainloop()

    def ask_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        self.color_label.configure(text=color[1])
        self.container.configure(fg_color=color[1])

    def ask_bg_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        self.configure(fg_color=color[1])
        self.frame.configure(fg_color=color[1])


if __name__ == '__main__':
    App()
