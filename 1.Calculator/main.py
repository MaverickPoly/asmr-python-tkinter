import customtkinter as ctk


def clear():
    var.set("")


def del_char():
    var.set(var.get()[:-1])


def percent():
    try:
        result = float(var.get()) / 100
        var.set(str(result))
    except:
        var.set("Error")


def add_char(char):
    var.set(var.get() + char)


def evaluate():
    try:
        result = eval(var.get())
        var.set(result)
    except:
        var.set("Error")


buttons_data = [
    [
        {"text": "C", "color": "red", "command": clear, "span": 1},
        {"text": "D", "color": "red", "command": del_char, "span": 1},
        {"text": "%", "color": "orange", "command": percent, "span": 1},
        {"text": "*", "color": "orange", "command": lambda: add_char("*"), "span": 1},
    ],
    [
        {"text": "7", "color": "grey", "command": lambda: add_char("7"), "span": 1},
        {"text": "8", "color": "grey", "command": lambda: add_char("8"), "span": 1},
        {"text": "9", "color": "grey", "command": lambda: add_char("9"), "span": 1},
        {"text": "/", "color": "orange", "command": lambda: add_char("/"), "span": 1},
    ],
    [
        {"text": "4", "color": "grey", "command": lambda: add_char("4"), "span": 1},
        {"text": "5", "color": "grey", "command": lambda: add_char("5"), "span": 1},
        {"text": "6", "color": "grey", "command": lambda: add_char("6"), "span": 1},
        {"text": "+", "color": "orange", "command": lambda: add_char("+"), "span": 1},
    ],
    [
        {"text": "1", "color": "grey", "command": lambda: add_char("1"), "span": 1},
        {"text": "2", "color": "grey", "command": lambda: add_char("2"), "span": 1},
        {"text": "3", "color": "grey", "command": lambda: add_char("3"), "span": 1},
        {"text": "-", "color": "orange", "command": lambda: add_char("-"), "span": 1},
    ],
    [
        {"text": "0", "color": "grey", "command": lambda: add_char("0"), "span": 1},
        {"text": ".", "color": "grey", "command": lambda: add_char("."), "span": 1},
        {"text": "=", "color": "orange", "command": evaluate, "span": 2},
    ]
]



window = ctk.CTk()
window.title("Calculator")
window.geometry("430x700")
window.eval()

var = ctk.StringVar(value="")

text_field = ctk.CTkEntry(
    master=window,
    fg_color="grey",
    height=100,
    font=("Comicsans", 40),
    corner_radius=20,
    textvariable=var,
    justify="right"
)
text_field.pack(fill="both", padx=20, pady=20)

btn_frame = ctk.CTkFrame(master=window, fg_color="#555")
btn_frame.pack(expand=True, fill="both", padx=20, pady=10)

for i, row in enumerate(buttons_data):
    for j, btn in enumerate(row):
        button = ctk.CTkButton(master=btn_frame, text=btn["text"], fg_color=btn["color"], font=("Arial", 34),
                               hover_color=btn["color"], command=btn["command"])
        button.grid(row=i, column=j, columnspan=btn["span"], sticky="nsew", padx=6, pady=6)


rows = len(buttons_data)
cols = len(buttons_data[0])
for i in range(rows):
    btn_frame.rowconfigure(i, weight=1)

for i in range(cols):
    btn_frame.columnconfigure(i, weight=1)


window.mainloop()
