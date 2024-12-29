import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog


class App(ctk.CTk):
    __filename__ = "text.txt"

    def __init__(self):
        super().__init__()

        self.title("Text Editor")
        self.geometry("1000x700")

        self.file_frame = ctk.CTkFrame(self)
        self.file_btn = ctk.CTkButton(self.file_frame, text="Open file", command=self.open_file)
        self.file_btn.pack()
        self.file_frame.pack(fill="x")

        self.text_box = ctk.CTkTextbox(self)
        self.text_box.bind("<Key>", self.save_data)
        self.text_box.pack(expand=True, fill="both")
        self.load_data()

        self.mainloop()

    def open_file(self):
        filename = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            self.__filename__ = filename
            self.load_data()

    def load_data(self):
        self.text_box.delete("1.0", "end")
        with open(self.__filename__, "r") as f:
            self.text_box.insert("1.0", f.read())

    def save_data(self, event: tk.Event):
        # print(event.keysym)
        with open(self.__filename__, "w") as f:
            f.write(self.text_box.get("1.0", "end"))


if __name__ == '__main__':
    App()
