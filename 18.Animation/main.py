import tkinter as tk

BALL_RADIUS = 40
WIDTH, HEIGHT = 1000, 700


class AnimationApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Colliding ball")

        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        start_x, start_y = WIDTH / 2 - BALL_RADIUS / 2, HEIGHT / 2 - BALL_RADIUS / 2

        self.speed_x = 5
        self.speed_y = 5
        self.ball = self.canvas.create_oval(
            start_x, start_y,
            start_x + BALL_RADIUS, start_y + BALL_RADIUS,
            fill="blue"
        )

        self.move_ball()

    def move_ball(self):
        coords = self.canvas.coords(self.ball)
        x1, y1, x2, y2 = coords

        if x1 <= 0 or x2 >= WIDTH:
            self.speed_x *= -1
        if y1 <= 0 or y2 >= HEIGHT:
            self.speed_y *= -1

        self.canvas.move(self.ball, self.speed_x, self.speed_y)
        self.root.after(20, self.move_ball)



if __name__ == '__main__':
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()
