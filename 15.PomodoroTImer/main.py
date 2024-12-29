import customtkinter as ctk
from plyer import notification

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.geometry("600x600")


        self.time_label = ctk.CTkLabel(self, text="No Timer!", font=("Arial", 40))
        self.time_label.pack(expand=True)

        self.input_frame = ctk.CTkFrame(self)
        self.text_field = ctk.CTkEntry(self.input_frame, placeholder_text="Enter time...")
        self.btn = ctk.CTkButton(self.input_frame, text="Start timer", command=self.start_timer)
        self.input_frame.pack(fill="x")
        self.text_field.pack(expand=True, side="left", fill="x", padx=8, pady=10)
        self.btn.pack(padx=10, pady=10)

        self.mainloop()

    def start_timer(self):
        try:
            self.time = int(self.text_field.get())
            self.text_field.delete(0, ctk.END)
            self.update_timer()
        except Exception as e:
            print(f"Error: {e}")

    def update_timer(self):
        if self.time > 0:
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_label.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.time -= 1
            self.after(1000, self.update_timer)
        else:
            self.time_label.configure(text="Time is up!")
            notification.notify(
                title="Time is out!",
                message="The Pomodoro timer has finished!",
                timeout=4,
                app_name="Pomodoro",
                ticker="Hello world",
                app_icon="./icon.ico"
            )


if __name__ == "__main__":
    App()
