import customtkinter as ctk
import speedtest
import threading


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Internet speed test")
        self.geometry("500x400")

        self.label = ctk.CTkLabel(self, text="Internet speed test", font=("Arial", 40))
        self.button = ctk.CTkButton(self, text="Test Speed", command=self.test_speed)
        self.speedtest = speedtest.Speedtest()

        self.label.pack(expand=True)
        self.button.pack(expand=True)

        self.mainloop()

    def test_speed(self):
        thread = threading.Thread(target=self.run_speedtest)
        thread.start()

    def run_speedtest(self):
        download_speed = self.speedtest.download() / 1000000
        self.label.configure(text=f"{round(download_speed, 1)} Mbps")


if __name__ == '__main__':
    app = App()
