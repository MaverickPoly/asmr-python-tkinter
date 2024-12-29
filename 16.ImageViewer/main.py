import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk


class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Image viewer")
		self.geometry("600x600")

		self.image_label = ctk.CTkLabel(self, text="")
		self.btn = ctk.CTkButton(self, text="Upload file", command=self.handle_upload)
		self.btn.pack(expand=True)

		self.mainloop()

	def handle_upload(self):
		file_path = filedialog.askopenfilename(title="Select an image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
		# image = ImageTk.PhotoImage(Image.open(file_path))
		image = Image.open(file_path)
		image = image.resize((400, 400))
		img = ctk.CTkImage(light_image=image, size=(400, 400))
		self.image_label.configure(image=img)
		self.image_label.pack(expand=True)


if __name__=="__main__":
	App()

