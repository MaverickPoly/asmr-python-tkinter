import customtkinter as ctk
from database import Database



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Todo List")
        self.geometry("500x600")
        self.db = Database()

        ctk.CTkLabel(self, text="Todo List", font=("Arial", 30)).pack()
        self.todo_frame = ctk.CTkFrame(self)
        self.todo_frame.pack(expand=True, fill="both")

        self.add_todo_ui()
        self.get_todos()

        self.mainloop()

    def get_todos(self):
        for widget in self.todo_frame.winfo_children():
            widget.destroy()

        todos = self.db.fetch()
        for todo in todos:
            uid, title, completed = todo
            todo_tile = TodoTile(self.todo_frame, title, bool(completed), uid, self.delete_todo, self.update_todo)
            todo_tile.pack(padx=8, pady=8, fill="x")

    def add_todo_ui(self):
        self.add_frame = ctk.CTkFrame(self)
        self.entry = ctk.CTkEntry(self.add_frame, placeholder_text="Enter a new todo")
        self.add_btn = ctk.CTkButton(self.add_frame, text="Add", command=self.add_todo)

        self.add_frame.pack(pady=6, side="bottom", fill="x")
        self.entry.pack(side="left", padx=10, expand=True, fill="x")
        self.add_btn.pack(side="left", padx=8)

    def add_todo(self):
        title = self.entry.get()
        if title:
            self.db.add(title, 0)
            self.get_todos()

    def delete_todo(self, uid):
        self.db.delete(uid)
        self.get_todos()

    def update_todo(self, uid, completed):
        todo = self.db.get(uid)
        if todo:
            self.db.update(uid, todo[1], completed)
            self.get_todos()


class TodoTile(ctk.CTkFrame):
    def __init__(self, master, title, completed, uid, on_delete, on_update):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=title, width=300, text_color="green" if completed else "red")
        self.label.pack(side="left")

        self.del_btn = ctk.CTkButton(self, text="🗑", command=lambda: on_delete(uid), width=40)
        self.del_btn.pack(side="right", padx=6)

        self.status_btn = ctk.CTkButton(
            self,
            text="Completed" if completed else "Uncompleted",
            command=lambda: on_update(uid, not completed)
        )
        self.status_btn.pack(side="right", padx=8)



if __name__ == '__main__':
    App()
