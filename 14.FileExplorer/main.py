import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class FileDialogApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("File Explorer")
        self.root.geometry("800x500")

        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.heading("#0", text="File Explorer", anchor="w")
        self.tree.column("#0", stretch=True, width=600)

        self.tree.bind("<<TreeviewOpen>>", self.on_open)
        self.populate_tree()

    def populate_tree(self, parent_id="", parent_path=""):
        if not parent_id:
            parent_id = ""
            parent_path = os.path.abspath(os.sep)

        if os.path.isdir(parent_path):
            try:
                for item in os.listdir(parent_path):
                    item_path = os.path.join(parent_path, item)
                    item_id = self.tree.insert(parent_id, "end", text=item, open=False)
                    if os.path.isdir(item_path):
                        self.tree.insert(item_id, "end", text="")
            except PermissionError:
                messagebox.showwarning("Permission Denied", f"Cannot access {parent_path}")

    def on_open(self, event):
        item_id = self.tree.focus()
        if not item_id:
            return

        children = self.tree.get_children(item_id)
        if len(children) == 1 and self.tree.item(children[0], "text") == "":
            self.tree.delete(children[0])

            path_parts = []
            current_item = item_id
            while current_item:
                path_parts.insert(0, self.tree.item(current_item, "text"))
                current_item = self.tree.parent(current_item)
            full_path = os.path.join(*path_parts)
            self.populate_tree(item_id, full_path)


if __name__ == '__main__':
    root = tk.Tk()
    app = FileDialogApp(root)
    root.mainloop()
