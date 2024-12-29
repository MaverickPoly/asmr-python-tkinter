import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
            {"question": "What is the largest of planet?", "options": ["Earth", "Mercury", "Jupyter", "Moon"], "answer": "Jupyter"},
            {"question": "Who is the founder of Python?", "options": ["Bjarne Stroustrup", "Einstein", "Guido Van Rossum", "Linus Torvalds"], "answer": "Guido Van Rossum"},
        ]

        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(self.root, text="Question will appear here...", font=("Arial", 25))
        self.question_label.pack(pady=10)

        self.selected_var = tk.StringVar()
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10, padx=10)

        self.buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.options_frame, variable=self.selected_var, text="", font=("Arial", 14), value="")
            button.pack(fill="x")
            self.buttons.append(button)

        self.submit_btn = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 18))
        self.submit_btn.pack(pady=10)
        self.next_question()

    def check_answer(self):
        selected_answer = self.selected_var.get()
        if selected_answer:
            correct_answer = self.questions[self.current_question_index]["answer"]
            if correct_answer == selected_answer:
                self.score += 1
            self.current_question_index += 1
            self.next_question()
        else:
            messagebox.showwarning("No selected", message="Please select one of the options...")

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.configure(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.buttons[i].configure(text=option, value=option)
                self.selected_var.set(option)
        else:
            self.handle_finish()

    def handle_finish(self):
        messagebox.showinfo("Quiz finished!", message=f"Correct: {self.score}/{len(self.questions)}")
        self.root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    QuizApp(root)
    root.mainloop()
