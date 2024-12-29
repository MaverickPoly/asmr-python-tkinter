import customtkinter as ctk
from database import Database



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Contact manager app")
        self.geometry("1000x700")
        self.db = Database()

        header_frame = ctk.CTkFrame(self)
        ctk.CTkLabel(header_frame, text="Contact Manager", font=("Arial", 30)).pack(expand=True, fill="x", side="left", pady=10)
        ctk.CTkButton(header_frame, text="Toggle", command=self.toggle_theme).pack(side="left", pady=10)
        header_frame.pack(fill="x")

        self.contacts_frame = ctk.CTkFrame(self)
        self.contacts_frame.pack(expand=True, fill="both")

        self.build_add_ui()
        self.fetch_contacts()


        self.mainloop()

    def fetch_contacts(self):
        for widget in self.contacts_frame.winfo_children():
            widget.destroy()

        contacts = self.db.fetch()
        for contact in contacts:
            tile = ContactTile(self.contacts_frame, self.on_delete, contact[1], contact[2], contact[0])
            tile.pack(fill="x")

    def build_add_ui(self):
        frame = ctk.CTkFrame(self)
        self.input_title = ctk.CTkEntry(frame, placeholder_text="Contact title")
        self.input_number = ctk.CTkEntry(frame, placeholder_text="Contact number")
        self.btn = ctk.CTkButton(frame, text="Add", command=self.add_contact)

        frame.pack(fill="x")
        self.input_title.pack(expand=True, fill="x", padx=8, pady=8,)
        self.input_number.pack(expand=True, fill="x", padx=8, pady=8, side="left")
        self.btn.pack(padx=8, pady=8)

    def on_delete(self, uid: int):
        self.db.delete(uid)
        self.fetch_contacts()

    def add_contact(self):
        title, number = self.input_title.get(), self.input_number.get()
        if title and number:
            self.db.add_item(title, number)
            self.fetch_contacts()
            self.input_title.delete(0, "end")

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")


class ContactTile(ctk.CTkFrame):
    def __init__(self, master, on_delete, title, number, uid):
        super().__init__(master=master)
        frame = ctk.CTkFrame(self, fg_color="transparent")
        title_label = ctk.CTkLabel(frame, text=title, font=("Arial", 16))
        number_label = ctk.CTkLabel(frame, text=number, font=("Arial", 13))
        delete = ctk.CTkButton(self, text="Delete", command=lambda: on_delete(uid))

        title_label.pack(expand=True, fill="x")
        number_label.pack(expand=True, fill="x")
        frame.pack(side="left", expand=True, fill="both")
        delete.pack(side="left", padx=10)




if __name__ == "__main__":
    App()
